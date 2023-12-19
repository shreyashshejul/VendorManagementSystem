# Create your views here.
# vendorapp/views.py
from datetime import timezone
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer
from .utils import calculate_performance_metrics

class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def retrieve(self, request, *args, **kwargs):
        vendor = self.get_object()
        performance_metrics = calculate_performance_metrics(vendor)
        serializer = self.get_serializer(vendor)
        response_data = serializer.data
        response_data.update(performance_metrics)
        return Response(response_data)

@api_view(['POST'])
def acknowledge_purchase_order(request, po_id):
    purchase_order = get_object_or_404(PurchaseOrder, pk=po_id)
    
    if request.method == 'POST':
        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()
        
        # Recalculate performance metrics
        vendor = purchase_order.vendor
        performance_metrics = calculate_performance_metrics(vendor)
        serializer = VendorSerializer(vendor)
        response_data = serializer.data
        response_data.update(performance_metrics)

        return Response(response_data, status=status.HTTP_200_OK)
