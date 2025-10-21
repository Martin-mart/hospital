from django.urls import path, include
from rest_framework import routers
from .views import InvoiceViewSet, invoice_list_view

router = routers.DefaultRouter()
router.register(r'api/invoices', InvoiceViewSet, basename='invoice')

app_name = 'billing'

urlpatterns = [
    path('invoices/', invoice_list_view, name='invoice_list_view'),
    path('', include(router.urls)),
]
