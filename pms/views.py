from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.shortcuts import render
from django.db import connection
import requests

def system_status_view(request):
    # Database check
    try:
        connection.ensure_connection()
        db_status = "Online"
    except Exception:
        db_status = "Offline"

    # API check
    try:
        response = requests.get("http://127.0.0.1:8000/appointments/api/appointments/")
        api_status = "Running" if response.status_code == 200 else "Down"
    except Exception:
        api_status = "Down"

    # Dummy checks
    security_status = "Active"
    performance_status = "Optimal"

    context = {
        "db_status": db_status,
        "security_status": security_status,
        "performance_status": performance_status,
        "api_status": api_status,
    }
    return render(request, "system_status.html", context)

def home(request):
    return render(request, "home.html")

def logout_view(request):
    logout(request)
    return redirect("home")  # "home" is the name of the home URL pattern
