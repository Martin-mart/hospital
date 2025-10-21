from django.urls import path, include
from rest_framework import routers
from .views import PatientProfileViewSet, MedicalRecordViewSet
router = routers.DefaultRouter()
router.register('profiles', PatientProfileViewSet)
router.register('records', MedicalRecordViewSet)
app_name = 'patients'
urlpatterns = [
    path('api/', include(router.urls)),
]
from django.urls import path, include
from rest_framework import routers
from .views import PatientProfileViewSet, MedicalRecordViewSet, patient_profiles_view

router = routers.DefaultRouter()
router.register('profiles', PatientProfileViewSet)
router.register('records', MedicalRecordViewSet)

app_name = 'patients'

urlpatterns = [
    # API routes
    path('api/', include(router.urls)),

    # Custom HTML route
    path('profiles/', patient_profiles_view, name='patient_profiles'),
]
