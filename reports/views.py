from django.shortcuts import render
from django.db.models import Sum
from appointments.models import Appointment
from billing.models import Invoice
from patients.models import PatientProfile
def daily_report(request):
    total_appointments = Appointment.objects.count()
    income = Invoice.objects.aggregate(total=Sum('amount'))['total'] or 0
    patients = PatientProfile.objects.count()
    context = {'total_appointments': total_appointments, 'income': income, 'patients': patients}
    return render(request, 'reports/daily.html', context)
