import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from formtools.wizard.views import SessionWizardView

from .forms import StepOneForm, StepTwoForm, StepThreeForm
from .models import Groomers, Appointment, Services


# Define the steps and forms for the wizard
FORMS = [
    ("step_one", StepOneForm),
    ("step_two", StepTwoForm),
    ("step_three", StepThreeForm),
]

# Define the templates correspondign to each step
TEMPLATES = {
    "step_one": "appointment/appointment_step_one.html",
    "step_two": "appointment/appointment_step_two.html",
    "step_three": "appointment/appointment_step_three.html",
}


class AppointmentWizard(LoginRequiredMixin, SessionWizardView):
    """
    View to habdle booking multistep form.
    Utilises Django Form Tools WizardView to manage form sessions.
    Sources: Medium and Django Formtools
    """
    form_list = FORMS

    def get_template_names(self):
        """
        Return the template name for the current step.
        """
        return [TEMPLATES[self.steps.current]]

    def get_form_kwargs(self, step):
        """
        Pass additional keyword arguments to forms in different steps.
        """
        kwargs = super().get_form_kwargs(step)
        if step == 'step_two':
            # Pass date from step one to step two
            date = self.get_cleaned_data_for_step('step_one')['date']
            kwargs['date'] = date
        if step == 'step_three':
            # Pass date and groomer from previous steps to step three
            cleaned_data = self.get_cleaned_data_for_step('step_one')
            date = cleaned_data['date']
            groomer = self.get_cleaned_data_for_step('step_two')['groomer']
            kwargs['date'] = date
            kwargs['groomer'] = groomer
        return kwargs

    def done(self, form_list, **kwargs):
        """
        Save the appointment when all steps are completed.
        """
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


@login_required
def my_appointments(request):
    """
    View to display the logged-in user's appointments.
    """
    update_past_appointments_status()

    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Check if the logged-in user is an admin
        if request.user.is_superuser:
            # Admin sees all appointments
            appointments = Appointment.objects.all().order_by('-date')
        else:
            # Regular users see only their own appointments
            appointments = (
                Appointment.objects.filter(user=request.user).order_by('-date')
            )
        now = timezone.now()

        # Add a flag to indicate if an appointment can be edited or deleted
        for appointment in appointments:
            # Combine the appointment date with a time (midnight)
            appointment_datetime = datetime.datetime.combine(
                appointment.date, datetime.time()
                )
            # Make the combined datetime timezone-aware
            appointment_datetime = timezone.make_aware(
                appointment_datetime, timezone.get_current_timezone()
                )
            appointment.can_edit_delete = (
                appointment_datetime - now).total_seconds() > 24 * 3600

        return render(request,
                      "appointment/my_appointments.html",
                      {'appointments': appointments})
    else:
        # If the user is not logged in, redirect them to the login page
        return redirect(reverse('account_login'))


@login_required
def update_past_appointments_status():
    """
    Function to update the status of past appointments to completed.
    """
    now = timezone.now()
    past_appointments = Appointment.objects.filter(
        date__lt=now.date(), status='scheduled'
        )
    past_appointments.update(status='completed')


@login_required
def appointment_delete(request, appointment_id):
    """
    View to delete an appointment.
    """
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    appointment.delete()
    messages.add_message(request, messages.SUCCESS, 'Appointment deleted!')

    return HttpResponseRedirect(reverse('my_appointments'))


@login_required
def edit_appointment(request, appointment_id):
    """
    View to handle the first step of editing an appointment.
    Sets session variables to pre-fill the edit form.
    """
    appointment = get_object_or_404(Appointment, id=appointment_id)

    # Save the relevant appointment details for future steps
    request.session['edit_appointment_id'] = appointment_id
    request.session['edit_service_id'] = appointment.service.id
    request.session['edit_date'] = appointment.date.strftime('%Y-%m-%d')
    request.session['edit_groomer_id'] = appointment.groomer.id
    request.session['edit_time'] = appointment.time.strftime('%H:%M')
    # Indicate the edit mode
    request.session['editing'] = True

    # Render the form for editing the appointment.
    return redirect('edit_appointment')


class EditAppointmentWizard(LoginRequiredMixin, SessionWizardView):
    """
    View to handle multi-step appointment editing.
    """
    form_list = FORMS

    def get_template_names(self):
        """
        Return the template name for the current step.
        """
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, form, **kwargs):
        """
        Pass additional context data to the template.
        """
        context = super().get_context_data(form=form, **kwargs)
        context['editing'] = self.request.session.get('editing', False)
        return context

    def get_form_initial(self, step):
        """
        Set initial form data based on the session variables.
        """
        initial = super().get_form_initial(step)

        if step == 'step_one':
            initial.update({
                'service': get_object_or_404(
                    Services, id=self.request.session['edit_service_id']),
                'date': datetime.datetime.strptime(
                    self.request.session['edit_date'], '%Y-%m-%d').date()
            })

        if step == 'step_two':
            initial.update({
                'groomer': get_object_or_404(
                    Groomers, id=self.request.session['edit_groomer_id']),
            })

        if step == 'step_three':
            initial.update({
                'time': self.request.session['edit_time']
            })

        return initial

    def get_form_kwargs(self, step):
        """
        Pass additional keyword arguments to forms in different steps.
        """
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
        """
        Update the appointment when all steps are completed.
        """
        form_data = [form.cleaned_data for form in form_list]
        service = form_data[0]['service']
        date = form_data[0]['date']
        groomer = form_data[1]['groomer']
        time = form_data[2]['time']

        # Update the existing appointment
        appointment_id = self.request.session['edit_appointment_id']
        appointment = get_object_or_404(Appointment, id=appointment_id)
        appointment.service = service
        appointment.date = date
        appointment.groomer = groomer
        appointment.time = time
        appointment.save()

        # Clear the session variable for editing mode
        del self.request.session['editing']

        messages.add_message(self.request, messages.SUCCESS,
                             "Appointment has been updated!")

        return redirect('my_appointments')
