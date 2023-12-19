# VendorManagementSystem
A Django-based Vendor Management System with RESTful API endpoints for managing vendors, purchase orders, and historical performance metrics.

Table of Contents
Installation
Usage
API Endpoints
Testing
Submission Guidelines
Installation
Clone the repository:

git clone https://github.com/shreyashshejul/VendorManagementSystem.git
Navigate to the project directory:


cd vendor-management-system
Install the required dependencies:

pip install -r requirements.txt
Apply database migrations:

python manage.py migrate
Create a superuser for admin access:

python manage.py createsuperuser
Follow the prompts to create a superuser account.

Run the development server:

python manage.py runserver
The server will be running at http://127.0.0.1:8000/.

Usage
Access the admin interface:

Navigate to http://127.0.0.1:8000/admin/ and log in with the superuser credentials created earlier.

Use the API endpoints:

The API endpoints are accessible at http://127.0.0.1:8000/api/. Refer to the API Endpoints section for details.

API Endpoints
Vendors
List/Create Vendors:

GET /api/vendors/ - List all vendors or POST /api/vendors/ - Create a new vendor.

Retrieve/Update/Delete Vendor:

GET /api/vendors/<vendor_id>/ - Retrieve details of a specific vendor.

PUT /api/vendors/<vendor_id>/ - Update details of a specific vendor.

DELETE /api/vendors/<vendor_id>/ - Delete a specific vendor.

Purchase Orders
List/Create Purchase Orders:

GET /api/purchase_orders/ - List all purchase orders or POST /api/purchase_orders/ - Create a new purchase order.

Retrieve/Update/Delete Purchase Order:

GET /api/purchase_orders/<po_number>/ - Retrieve details of a specific purchase order.

PUT /api/purchase_orders/<po_number>/ - Update details of a specific purchase order.

DELETE /api/purchase_orders/<po_number>/ - Delete a specific purchase order.

Historical Performance
List Historical Performances:

GET /api/historical_performances/ - List all historical performance metrics.

Testing
To run the test suite, use the following command:

python manage.py test vendor_app.tests
