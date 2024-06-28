from django.urls import path
from .views import (
     AppointmentWizard,
     my_appointments,
     appointment_delete,
)

from .forms import StepOneForm, StepTwoForm, StepThreeForm

FORMS = [
    ("step_one", StepOneForm),
    ("step_two", StepTwoForm),
    ("step_three", StepThreeForm),
]

urlpatterns = [
    path('', AppointmentWizard.as_view(FORMS), name='appointment'),
    path('my-appointments/', my_appointments, name='my_appointments'),
    path('appointment_delete/<int:appointment_id>/',
         appointment_delete, name='appointment_delete'),
]
