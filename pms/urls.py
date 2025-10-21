from django.contrib import admin
from django.urls import path, include
from accounts import views   # import views from the accounts app
from .views import system_status_view

urlpatterns = [
    path("", views.home, name="home"),  # root URL -> home view
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('system-status/', system_status_view, name='system_status'),
    path("patients/", include("patients.urls")),
    path("appointments/", include("appointments.urls")),
    path("billing/", include("billing.urls")),
]
