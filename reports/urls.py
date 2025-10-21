from django.urls import path
from .views import daily_report
app_name = 'reports'
urlpatterns = [
    path('daily/', daily_report, name='daily_report'),
]
