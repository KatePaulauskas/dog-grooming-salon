from .models import Appointment, Services
from django import forms
import datetime

# Form for booking appointments with dynamic time slot choices.

class AppointmentForm(forms.ModelForm):
    """
    Specifies how date and time fields should be handled within the form 
    Sets date field with Calendar widget
    Sources: 
    https://pythonassets.com/posts/date-field-with-calendar-widget-in-django-forms/
    https://docs.djangoproject.com/en/5.0/ref/forms/fields/
    """
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.ChoiceField(choices=[])

    class Meta:
        model = Appointment
        fields = ('service', 'groomer', 'date', 'time')
    
    # Updates the 'time' field choices with available time slots.
    def set_time_choices(self, choices):
        self.fields['time'].choices = choices