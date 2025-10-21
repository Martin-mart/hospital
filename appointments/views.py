from rest_framework import viewsets, generics
from django.shortcuts import render
from .models import Appointment
from .serializers import AppointmentSerializer

# API view (Django REST Framework)
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by('-scheduled_time')
    serializer_class = AppointmentSerializer


# Simple API endpoint for list/create
class AppointmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all().order_by('-scheduled_time')
    serializer_class = AppointmentSerializer


# HTML view (User-friendly interface)
def appointment_list_view(request):
    appointments = Appointment.objects.all().order_by('-scheduled_time')[:10]
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})
