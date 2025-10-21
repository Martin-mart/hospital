from rest_framework import serializers
from .models import PatientProfile, MedicalRecord
class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'
class PatientProfileSerializer(serializers.ModelSerializer):
    records = MedicalRecordSerializer(many=True, read_only=True)
    class Meta:
        model = PatientProfile
        fields = ('id', 'user', 'dob', 'address', 'emergency_contact', 'records')
