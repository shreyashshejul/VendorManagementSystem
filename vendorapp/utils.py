# vendorapp/utils.py
from django.utils import timezone
from django.db.models import Avg, F
from .models import PurchaseOrder

def calculate_performance_metrics(vendor_instance):
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor_instance, status='completed')
    total_completed_orders = completed_orders.count()

    if total_completed_orders == 0:
        return {
            'on_time_delivery_rate': 0,
            'quality_rating_avg': None,
            'average_response_time': None,
            'fulfillment_rate': 0,
        }

    on_time_delivery_count = completed_orders.filter(delivery_date__lte=timezone.now()).count()
    on_time_delivery_rate = (on_time_delivery_count / total_completed_orders) * 100

    quality_rating_avg = completed_orders.exclude(quality_rating__isnull=True).aggregate(avg_quality=Avg('quality_rating'))['avg_quality']

    average_response_time = completed_orders.exclude(acknowledgment_date__isnull=True).exclude(issue_date__isnull=True).aggregate(avg_response_time=Avg(F('acknowledgment_date') - F('issue_date')))['avg_response_time']

    fulfillment_rate = (completed_orders.filter(status='completed').count() / total_completed_orders) * 100

    return {
        'on_time_delivery_rate': on_time_delivery_rate,
        'quality_rating_avg': quality_rating_avg,
        'average_response_time': average_response_time.total_seconds() if average_response_time else None,
        'fulfillment_rate': fulfillment_rate,
    }
