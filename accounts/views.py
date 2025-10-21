from datetime import date
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Patient
from appointments.models import Appointment
from django.contrib.auth import logout

# Import models
from .models import Patient, Appointment, MedicalRecord


# Logout view
def logout_view(request):
    logout(request)
    return redirect("login")  # After logout, send back to login page


# Home page
def home(request):
    return render(request, "accounts/home.html")


# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Superusers or staff always go to admin dashboard
            if user.is_superuser or user.is_staff:
                return redirect("admin_dashboard")

            # Redirect based on group
            if user.groups.filter(name="Admin").exists():
                return redirect("admin_dashboard")
            elif user.groups.filter(name="Doctor").exists():
                return redirect("doctor_dashboard")
            elif user.groups.filter(name="Nurse").exists():
                return redirect("nurse_dashboard")
            elif user.groups.filter(name="Receptionist").exists():
                return redirect("receptionist_dashboard")
            elif user.groups.filter(name="Patient").exists():
                return redirect("patient_dashboard")
            else:
                return HttpResponse("You don’t have permission to view or edit anything.")

        else:
            return render(
                request,
                "accounts/login.html",
                {"error": "Invalid username or password"},
            )

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
def admin_dashboard(request):
    from django.db import connection
    import requests

    # Check database connection
    try:
        connection.ensure_connection()
        db_status = "Online"
    except Exception:
        db_status = "Offline"

    # Check API status
    try:
        response = requests.get("http://127.0.0.1:8000/appointments/api/appointments/")
        api_status = "Running" if response.status_code == 200 else "Down"
    except Exception:
        api_status = "Down"

    # Static checks for now
    security_status = "Active"
    performance_status = "Optimal"

    # Get recent appointments
    appointments = Appointment.objects.all().order_by('-date', '-time')[:10]

    context = {
        "appointments": appointments,
        "db_status": db_status,
        "security_status": security_status,
        "performance_status": performance_status,
        "api_status": api_status,
    }

    return render(request, "accounts/dashboards/admin_dashboard.html", context)

# Doctor dashboard
@login_required
def doctor_dashboard(request):
    todays_patients = Appointment.objects.filter(
        doctor=request.user,
        date=date.today()
    ).count()

    waiting_now = Appointment.objects.filter(
        doctor=request.user,
        status="waiting"
    ).count()

    todays_appointments = Appointment.objects.filter(
        doctor=request.user,
        date=date.today()
    )

    pending_charts = MedicalRecord.objects.filter(
        doctor=request.user,
        status="pending"
    ).count()

    context = {
        "todays_patients": todays_patients,
        "waiting_now": waiting_now,
        "todays_appointments": todays_appointments.count(),
        "pending_charts": pending_charts,
        "patient_list": Patient.objects.filter(appointments__doctor=request.user).distinct()[:10],
        "appointments": todays_appointments,
        "records": MedicalRecord.objects.filter(doctor=request.user)[:5],
    }
    return render(request, "accounts/dashboards/doctor_dashboard.html", context)


# Nurse dashboard
@login_required
def nurse_dashboard(request):
    return render(request, "accounts/dashboards/nurse_dashboard.html")


# Receptionist dashboard
@login_required
def receptionist_dashboard(request):
    return render(request, "accounts/dashboards/receptionist_dashboard.html")


# Patient dashboard
@login_required
def patient_dashboard(request):
    return render(request, "accounts/dashboards/patient_dashboard.html")


# Role-based redirect
@login_required
def dashboard(request):
    if request.user.is_superuser or request.user.is_staff:
        return redirect("admin_dashboard")
    if request.user.groups.filter(name="Doctor").exists():
        return redirect("doctor_dashboard")
    if request.user.groups.filter(name="Nurse").exists():
        return redirect("nurse_dashboard")
    if request.user.groups.filter(name="Receptionist").exists():
        return redirect("receptionist_dashboard")
    if request.user.groups.filter(name="Patient").exists():
        return redirect("patient_dashboard")
    return redirect("home")

@login_required
@permission_required('accounts.add_patientnote', raise_exception=True)
def add_patient_note(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        note_text = request.POST.get('note')
        if note_text:
            PatientNote.objects.create(patient=patient, doctor=request.user, note=note_text)
            return redirect('doctor_dashboard')
    return render(request, 'accounts/add_patient_note.html', {'patient': patient})