from django import forms
from django.contrib import messages
from .models import Appointment, Services, Groomers
import datetime
from datetime import date, time, datetime, timedelta
from django.core.exceptions import ValidationError


class StepOneForm(forms.ModelForm):
    """
    Specifies how date and time fields should be handled within the form
    Sets date field with Calendar widget.
    Sources: Python Assets & Django Documentation - Form fields
    """
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Appointment
        fields = ('service', 'date',)

    """
    Prevent date booking in the past or
    more than 90 days in advance
    Source: Stack Overflow
    """
    def clean_date(self):
        selected_date = self.cleaned_data.get('date')
        today = date.today()
        now = datetime.now()

        # Define closing times for weekdays and weekends
        weekday_closing_time = time(17, 30)
        weekend_closing_time = time(16, 0)

        if selected_date < today:
            raise ValidationError("Not possible to select date in the past")

        # Determine closing time based on the day of the week
        if selected_date.weekday() < 5:
            closing_time = weekday_closing_time
        else:
            closing_time = weekend_closing_time
            
        if selected_date == today and now.time() > closing_time:
            raise ValidationError(
                "Not possible to book for today as the salon is already closed")

        elif selected_date > today + timedelta(days=90):
            raise ValidationError(
                "Not possible to select a date more than 90 days in advance")

        return selected_date


class StepTwoForm(forms.ModelForm):
    groomer = forms.ModelChoiceField(queryset=Groomers.objects.none())

    class Meta:
        model = Appointment
        fields = ('groomer',)

    def __init__(self, *args, **kwargs):
        date = kwargs.pop('date', None)
        super().__init__(*args, **kwargs)
        if date:
            self.fields['groomer'].queryset = self.get_available_groomers(date)

    def get_available_groomers(self, date):
        available_groomers = []
        all_groomers = Groomers.objects.all()
        for groomer in all_groomers:
            start_time, end_time = self.get_groomer_schedule(groomer, date)
            if start_time and end_time:
                available_groomers.append(groomer)
        return Groomers.objects.filter(
            id__in=[g.id for g in available_groomers])

    def get_groomer_schedule(self, groomer, date):
        """
        Retrieves the groomer's start and end times for a specific day.
        Converts the date into the day of the week and dynamically fetches
        the corresponding start and end times of the groomer.
        Sources:  Programiz and Stack Overflow
        """
        day_name = date.strftime('%A').lower()
        schedule = groomer.schedule
        start_time = getattr(schedule, f'{day_name}_start')
        end_time = getattr(schedule, f'{day_name}_end')
        return start_time, end_time


class StepThreeForm(forms.Form):
    time = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):

        groomer = kwargs.pop('groomer', None)
        date = kwargs.pop('date', None)
        # Call the parent class's __init__ method
        super().__init__(*args, **kwargs)

        if groomer and date:
            self.fields['time'].choices = self.generate_time_choices(
                groomer, date
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
        now = datetime.now()

        # Generate the list of time slots
        while start_datetime < end_datetime:
            # Convert start time into '09:30' format
            time_str = start_datetime.time().strftime('%H:%M')
            if date == date.today() and start_datetime < now:
                start_datetime += interval
                continue
            if self.is_groomer_available(groomer, date, start_datetime.time()):
                times.append((time_str, time_str))
            start_datetime += interval

        return times

    def get_groomer_schedule(self, groomer, date):
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
