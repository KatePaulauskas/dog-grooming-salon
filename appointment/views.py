from django.shortcuts import render
from django.contrib import messages
from .forms import StepOneForm
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

def book_appointment_step_one(request):
    """
    Handle the first step of the appointment booking process.
    Users select a service, groomer, and date.
    """
    if request.method == 'POST':
        form_step_one = StepOneForm(data=request.POST)
        if form_step_one.is_valid():

            """
            Store selected service, groomer, and date in the session to be used in the next step
            Sources:
            https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78
            https://docs.djangoproject.com/en/5.0/topics/forms/
            https://docs.djangoproject.com/en/5.0/ref/forms/validation/
            """

            # Retrieve service and groomer id from the cleaned data
            request.session['service_id'] = form_step_one.cleaned_data['service'].id
            request.session['groomer_id'] = form_step_one.cleaned_data['groomer'].id

            # Convert the date to a string format for consistent storage in the session
            request.session['date'] = form_step_one.cleaned_data['date'].strftime('%Y-%m-%d')
            
            return redirect('book_appointment_step_two') 
    else:
        # Create an empty form for GET request
        form_step_one = StepOneForm()
    return render(
        request, 
        "appointment/appointment_step_one.html", 
        {
            'form_step_one': form_step_one
            }
    )
