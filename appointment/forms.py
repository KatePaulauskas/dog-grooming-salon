from django import forms
from django.contrib import messages
from .models import Appointment, Services, Groomers
import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta
from django.core.exceptions import ValidationError
# Form for booking appointments with dynamic time slot choices.


class StepOneForm(forms.ModelForm):
    """
    Specifies how date and time fields should be handled within the form
    Sets date field with Calendar widget.
    Sources:
    https://pythonassets.com/posts/date-field-with-calendar-widget-in-django-forms/
    https://docs.djangoproject.com/en/5.0/ref/forms/fields/
    """
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Appointment
        fields = ('service', 'groomer', 'date',)

    """
    Prevent date booking in the pasr or
    more than 90 days in advance
    Source:
    https://stackoverflow.com/questions/4941974/
    django-how-to-set-datefield-to-only-accept-today-future-dates
    """
    def clean_date(self):
        selected_date = self.cleaned_data.get('date')
        today = date.today()

        if selected_date < today:
            raise ValidationError("Not possible to select date in the past")

        elif selected_date > today + timedelta(days=90):
            raise ValidationError
            ("Not possible to select a date more than 90 days in advance")

        return selected_date


class StepTwoForm(forms.ModelForm):
    time = forms.ChoiceField(choices=[])

    class Meta:
        model = Appointment
        fields = ('time',)

    def __init__(self, *args, **kwargs):
        """
        Store request object for messages
        source:
        https://sayari3.com/articles/16-how-to-pass-user-object-to-django-form/
        """
        self.request = kwargs.pop('request')
        self.groomer = kwargs.pop('groomer')
        self.date = kwargs.pop('date')
        # Call the parent class's __init__ method
        super().__init__(*args, **kwargs)

        if self.groomer and self.date:
            self.fields['time'].choices = self.generate_time_choices(
                self.groomer, self.date
                )

    def generate_time_choices(self, groomer, date):
        """
        Generate a list of available time slots
        for a specific groomer and date.
        """
        # Identify start and end time for each groomer
        start_time, end_time = self.get_groomer_schedule(groomer, date)

        # Warn user if groomer is not available
        if not start_time or not end_time:
            messages.add_message
            (self.request, messages.WARNING,
             "The selected groomer is not available on the chosen date.")
            return []

        # Combine date with start time and end time to create datetime objects
        start_datetime = datetime.combine(date, start_time)
        end_datetime = datetime.combine(date, end_time)

        """
        Create time intervals of 2 hours,
        accountign for 30 min buffer time after each session
        """
        interval = timedelta(hours=2)
        times = []

        # Generate the list of time slots
        while start_datetime < end_datetime:
            # Convert start time into '09:30' format
            time_str = start_datetime.time().strftime('%H:%M')
            current_time = start_datetime.time()
            if self.is_groomer_available(groomer, date, current_time):
                times.append((time_str, time_str))
            start_datetime += interval

        return times

    def get_groomer_schedule(self, groomer, date):
        """
        Retrieves the groomer's start and end times for a specific day.
        Converts the date into the day of the week and dynamically fetches
        the corresponding start and end times of the groomer.
        Sources:
        https://www.programiz.com/python-programming/datetime/strftime
        https://stackoverflow.com/questions/51905712/
        how-to-get-the-value-of-a-django-model-field-object
        """
        day_name = date.strftime('%A').lower()
        schedule = groomer.schedule
        start_time = getattr(schedule, f'{day_name}_start')
        end_time = getattr(schedule, f'{day_name}_end')
        return start_time, end_time

    def is_groomer_available(self, groomer, date, time):
        """
        Check if the groomer is available at a specific date and time.
        """
        appointments = Appointment.objects.filter(groomer=groomer,
                                                  date=date, time=time)
        return not appointments.exists()
