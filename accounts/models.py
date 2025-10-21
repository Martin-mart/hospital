from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Roles available in the system
ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('doctor', 'Doctor'),
    ('nurse', 'Nurse'),
    ('receptionist', 'Receptionist'),
    ('patient', 'Patient'),
]


class User(AbstractUser):
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)

    def is_doctor(self):
        return self.role == 'doctor'

    def is_nurse(self):
        return self.role == 'nurse'

    def is_receptionist(self):
        return self.role == 'receptionist'

    def is_patient(self):
        return self.role == 'patient'

    def __str__(self):
        return f"{self.username} ({self.role})"


class Patient(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments")
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={"role": "doctor"}, related_name="doctor_appointments")
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[("waiting", "Waiting"), ("completed", "Completed")], default="waiting")

    def __str__(self):
        return f"{self.patient.user.username} with Dr.{self.doctor.username} on {self.date}"


class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="medical_records")
    doctor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"role": "doctor"},
        related_name="doctor_records"  # UNIQUE related_name to avoid clash
    )
    diagnosis = models.TextField()
    treatment = models.TextField()
    status = models.CharField(max_length=20, choices=[("pending", "Pending"), ("reviewed", "Reviewed")], default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Record for {self.patient.user.username} on {self.created_at.date()}"

class PatientNote(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="notes")
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notes")
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note by {self.doctor} on {self.patient}"