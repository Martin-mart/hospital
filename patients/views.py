from rest_framework import viewsets
from django.shortcuts import render
from .models import PatientProfile, MedicalRecord
from .serializers import PatientProfileSerializer, MedicalRecordSerializer

# API viewsets
class PatientProfileViewSet(viewsets.ModelViewSet):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

# HTML view
def patient_profiles_view(request):
    profiles = PatientProfile.objects.all()
    return render(request, 'patients/patient_profiles.html', {'profiles': profiles})
