from django.shortcuts import render
from .forms import AppointmentForm

def book_appointment(request):
    appointment_form = AppointmentForm()

    return render(
        request,
        "appointment/appointment.html",
        {
            "appointment_form": appointment_form,
        },
    )
