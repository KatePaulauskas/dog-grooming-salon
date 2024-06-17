from django.shortcuts import render
from django.contrib import messages
from .forms import AppointmentForm
import datetime

"""
Create a list of 30-minute time slots for a single day, 
starting at 9:00 AM and ending at 5:00 PM.
"""
def generate_time_choices():
    # Define the start and end time of appointments
    start_time = datetime.time(9, 0)
    end_time = datetime.time(17, 0)
    # Define interval between appointments
    interval = datetime.timedelta(minutes=30)
    times = []
    # Combine today's date with the start time
    current_datetime = datetime.datetime.combine(datetime.date.today(), start_time)
    # Combine today's date with the end time
    end_datetime = datetime.datetime.combine(datetime.date.today(), end_time)

    # Generate time slots between the start and end times
    while current_datetime < end_datetime:
        times.append((current_datetime.time().strftime('%H:%M'), current_datetime.time().strftime('%H:%M')))
        current_datetime += interval

    return times

def book_appointment(request):
    # Generate time choices for the form
    time_choices = generate_time_choices()

    if request.method == 'POST':
        appointment_form = AppointmentForm(data=request.POST)
        # Update time choices before processing form
        appointment_form.set_time_choices(time_choices)

        if appointment_form.is_valid():
            # Create the booking but don't save it to the database yet
            appointment = appointment_form.save(commit=False)
            # Set the user to the current user to ensure user is included into the booking form
            appointment.user = request.user
            appointment_form.save()
            # Add success message
            messages.add_message(request, messages.SUCCESS, "Thank you for booking your appointment!")
            # Reset the form to clear input fields
            appointment_form = AppointmentForm()
            # Reset time choices
            appointment_form.set_time_choices(time_choices)  

    return render(
        request,
        "appointment/appointment.html",
        {
            "appointment_form": appointment_form,
        },
    )
