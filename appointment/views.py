from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import StepOneForm, StepTwoForm
from django.http import HttpResponseRedirect
from .models import Groomers, Appointment, Services
import datetime
from django.urls import reverse

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

def book_appointment_step_two(request):
    """
    Handle the second step of the appointment booking process.
    Users select an available time slot.
    """
    # Retrieve stored service, groomer, and date from the session
    service_id = request.session.get('service_id')
    groomer_id = request.session.get('groomer_id')
    date_str = request.session.get('date')

    """
    Retrieve the specified Services and Groomers objects using the IDs stored in the session 
    If no object is found with the given ID, 404 error is raised
    Source: 
    https://www.geeksforgeeks.org/get_object_or_404-method-in-django-models/
    """
    service = get_object_or_404(Services, id=service_id)
    groomer = get_object_or_404(Groomers, id=groomer_id)
    
    # Convert the date string back to a date object to ensure that date operations can be performed correctly
    
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

    if request.method == 'POST':
        form_step_two = StepTwoForm(data=request.POST, groomer=groomer, date=date, request=request)
        if form_step_two.is_valid():
            # Create and save the new appointment
            appointment = form_step_two.save(commit=False)
            appointment.service = service
            appointment.groomer = groomer
            appointment.date = date
            appointment.user = request.user
            appointment.save()
            messages.add_message(request, messages.SUCCESS, "Thank you for booking your appointment!")

            # Redirect to booked appointments
            return redirect('my_appointments')

    else:
        # Create an empty form
        form_step_two = StepTwoForm(groomer=groomer, date=date, request=request)
 

    return render(
        request, 
        "appointment/appointment_step_two.html", 
        {
            'form_step_two': form_step_two, 'service': service, 
            'groomer': groomer, 'date': date
            }
    )

def my_appointments(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Get all appointments for the logged-in user, ordered by date ascending
        appointments = Appointment.objects.filter(user=request.user).order_by('date')
        return render(request,
        "appointment/my_appointments.html",
        {'appointments': appointments
        }
    )
    else:
        # If the user is not logged in, redirect them to the login page
        return redirect(reverse('account_login'))

def appointment_delete(request, appointment_id):
    """
    View to delete an appointment.
    """
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    
    appointment.delete()
    
    messages.add_message(request, messages.SUCCESS, 'Appointment deleted!')

    return HttpResponseRedirect(reverse('my_appointments'))

