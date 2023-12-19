# vendorapp/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from vendorapp.models import Vendor, PurchaseOrder

class PurchaseOrderAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor = Vendor.objects.create(name='Vendor 1', contact_details='Contact 1', address='Address 1', vendor_code='VENDOR001')
        self.po_data = {'po_number': 'PO001', 'vendor': self.vendor, 'order_date': '2023-01-01T12:00:00Z',
                        'delivery_date': '2023-01-10T12:00:00Z', 'items': {'item1': 5}, 'quantity': 5, 'status': 'pending'}
        self.purchase_order = PurchaseOrder.objects.create(**self.po_data)

    def test_retrieve_purchase_order(self):
        purchase_order_id = self.purchase_order.id
        response = self.client.get(reverse('purchase-order-retrieve-update-delete', args=[purchase_order_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_purchase_order_invalid_argument(self):
        invalid_id = 999999
        response = self.client.get(reverse('purchase-order-retrieve-update-delete', args=[invalid_id]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class VendorAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor_data = {'name': 'Vendor 1', 'contact_details': 'Contact 1', 'address': 'Address 1', 'vendor_code': 'VENDOR001'}

    def test_create_vendor(self):
        response = self.client.post(reverse('vendor-list-create'), self.vendor_data, format='json')
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_vendor(self):
        vendor = Vendor.objects.create(**self.vendor_data)
        response = self.client.get(reverse('vendor-retrieve-update-delete', args=[vendor.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
