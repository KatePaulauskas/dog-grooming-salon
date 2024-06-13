from django.shortcuts import render
from django.contrib import messages
from .forms import AppointmentForm

def book_appointment(request):
    appointment_form = AppointmentForm()

    if request.method == "POST":
        appointment_form = AppointmentForm(data=request.POST)
        if appointment_form.is_valid():
            # Create the object but don't save it to the database yet
            appointment = appointment_form.save(commit=False)
            # Set the user to the current user to ensure user is included into the booking form 
            appointment.user = request.user
            appointment_form.save()
            messages.add_message(request, messages.SUCCESS, "Thank you for booking your appointment!")
            # Reset the form to clear input fields
            appointment_form = AppointmentForm()

    return render(
        request,
        "appointment/appointment.html",
        {
            "appointment_form": appointment_form,
        },
    )

