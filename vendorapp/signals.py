# vendorapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder
from .utils import calculate_performance_metrics
from vendorapp.models import Vendor

@receiver(post_save, sender=PurchaseOrder)
def update_metrics_on_purchase_order_save(sender, instance, **kwargs):
    if instance.status == 'completed' and kwargs.get('update_fields') is None:
        
        vendor = instance.vendor
        performance_metrics = calculate_performance_metrics(vendor)

        Vendor.objects.filter(pk=vendor.pk).update(
            on_time_delivery_rate=performance_metrics['on_time_delivery_rate'],
            quality_rating_avg=performance_metrics['quality_rating_avg'],
            average_response_time=performance_metrics['average_response_time'],
            fulfillment_rate=performance_metrics['fulfillment_rate'],
        )
