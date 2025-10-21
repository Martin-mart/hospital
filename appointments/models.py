from django.db import models
from django.conf import settings
from patients.models import PatientProfile
STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('cancelled', 'Cancelled'),
    ('completed', 'Completed'),
]
class Appointment(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='appointments')
    scheduled_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True, null=True)
    def __str__(self):
        return f'Appt {self.id} {self.patient.user.username} with {self.doctor.username if self.doctor else "-"} at {self.scheduled_time}'
