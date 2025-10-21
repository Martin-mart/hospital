from django.db import models
from patients.models import PatientProfile
class Invoice(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return f'Invoice {self.id} for {self.patient.user.username}'
