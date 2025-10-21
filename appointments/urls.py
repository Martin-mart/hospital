from django.urls import path, include
from rest_framework import routers
from . import views
from .views import AppointmentViewSet, appointment_list_view

router = routers.DefaultRouter()
router.register('appointments', AppointmentViewSet)

app_name = 'appointments'

urlpatterns = [
    path('api/', include(router.urls)),
    path('', appointment_list_view, name='appointment_list_view'),
]
