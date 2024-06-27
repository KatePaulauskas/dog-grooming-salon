from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import StepOneForm, StepTwoForm, StepThreeForm
from django.http import HttpResponseRedirect
from .models import Groomers, Appointment, Services
import datetime
from django.urls import reverse
from formtools.wizard.views import SessionWizardView


FORMS = [
    ("step_one", StepOneForm),
    ("step_two", StepTwoForm),
    ("step_three", StepThreeForm),
]

TEMPLATES = {
    "step_one": "appointment/appointment_step_one.html",
    "step_two": "appointment/appointment_step_two.html",
    "step_three": "appointment/appointment_step_three.html",
}


class AppointmentWizard(SessionWizardView):
    """
    View to habdle booking multistep form
    Source:
    https://django-formtools.readthedocs.io/en/latest/wizard.html
    """
    form_list = FORMS

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_form_kwargs(self, step):
        kwargs = super().get_form_kwargs(step)
        if step == 'step_two':
            date = self.get_cleaned_data_for_step('step_one')['date']
            kwargs['date'] = date
        if step == 'step_three':
            cleaned_data = self.get_cleaned_data_for_step('step_one')
            date = cleaned_data['date']
            groomer = self.get_cleaned_data_for_step('step_two')['groomer']
            kwargs['date'] = date
            kwargs['groomer'] = groomer
        return kwargs

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        service = form_data[0]['service']
        date = form_data[0]['date']
        groomer = form_data[1]['groomer']
        time = form_data[2]['time']

        # Save the appointment
        appointment = Appointment(
            user=self.request.user,
            service=service,
            date=date,
            groomer=groomer,
            time=time
        )
        appointment.save()

        messages.add_message(self.request, messages.SUCCESS,
                             "Thank you for booking your appointment!")
        return redirect('my_appointments')


def my_appointments(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        """"
        View to dispaly existing bookings.
        Get all appointments for the logged-in user,
        ordered by date ascending
        """
        appointments = (
            Appointment.objects.filter(user=request.user).order_by('date')
            )
        return render(request,
                      "appointment/my_appointments.html",
                      {'appointments': appointments})
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


"""
def edit_appointment_step_one(request, appointment_id):

    View to handle the first step of editing an appointment.
    If the request method is GET, it pre-fills the form
    with the current appointment details and renders the form for editing.
    If the form is submitted via POST request, it validates the form data and,
    if valid, saves the relevant details to the session and redirects the user
    to the second step of the edit process.

    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'POST':
        # Initialize the form with the existing appointment details
        form_step_one = StepOneForm(data=request.POST, instance=appointment)
        if form_step_one.is_valid():
            # Save the relevant appointment details to the session.
            request.session['edit_appointment_id'] = appointment_id
            request.session['service_id'] = (
                form_step_one.cleaned_data['service'].id
                )
            request.session['groomer_id'] = (
                form_step_one.cleaned_data['groomer'].id
                )
            request.session['date'] = (
                form_step_one.cleaned_data['date'].strftime('%Y-%m-%d')
            )
            # Redirect to the second step of the edit process.
            return redirect('edit_appointment_step_two')

    else:
        form_step_one = StepOneForm(instance=appointment)

    # Render the form for editing the appointment.
    return render(
        request,
        "appointment/edit_appointment_step_one.html",
        {'form_step_one': form_step_one,
         'appointment_id': appointment_id})


def edit_appointment_step_two(request):

    View to handle the second step of editing an appointment.

    # Retrieve the appointment ID from the session
    appointment_id = request.session.get('edit_appointment_id')

    # Get the appointment object, or return a 404 error if not found
    appointment = get_object_or_404(Appointment, pk=appointment_id)

    # Retrieve service, groomer, and date information from the session
    service_id = request.session.get('service_id')
    groomer_id = request.session.get('groomer_id')
    date_str = request.session.get('date')

    # Get the service and groomer objects, or return a 404 error if not found
    service = get_object_or_404(Services, id=service_id)
    groomer = get_object_or_404(Groomers, id=groomer_id)

    # Convert the date string back to a date object
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

    # Check if the form has been submitted via POST request
    if request.method == 'POST':
        # Initialise the form with the submitted data, groomer, and date.
        form_step_two = StepTwoForm(data=request.POST, groomer=groomer,
                                    date=date, request=request)

        # Validate the form
        if form_step_two.is_valid():
            # Update the appointment with the new details
            appointment.service = service
            appointment.groomer = groomer
            appointment.date = date
            appointment.time = form_step_two.cleaned_data['time']
            appointment.save()

            # Add a success message
            messages.add_message(request, messages.SUCCESS,
                                 "Your appointment is updated!")

            # Redirect to the user's appointments page
            return redirect('my_appointments')
    else:
        # Initialise the form with the current appointment details
        form_step_two = StepTwoForm(groomer=groomer, date=date,
                                    request=request, instance=appointment)

    # Render the template with the form and context data
    return render(
        request,
        "appointment/edit_appointment_step_two.html",
        {'form_step_two': form_step_two,
         'service': service,
         'groomer': groomer,
         'date': date,
         # Pass the appointment_id to the template context
         'appointment_id': appointment_id})
"""
