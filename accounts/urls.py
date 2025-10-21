from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    # Dashboards
    path("admin/dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("doctor/dashboard/", views.doctor_dashboard, name="doctor_dashboard"),
    path("doctor/patient/<int:patient_id>/add-note/", views.add_patient_note, name="add_patient_note"),
    path("nurse/dashboard/", views.nurse_dashboard, name="nurse_dashboard"),
    path("receptionist/dashboard/", views.receptionist_dashboard, name="receptionist_dashboard"),
    path("patient/dashboard/", views.patient_dashboard, name="patient_dashboard"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
