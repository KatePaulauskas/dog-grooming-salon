from django.contrib import admin
from .models import Groomers, GroomerSchedule

@admin.register(Groomers)
class GroomersAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

@admin.register(GroomerSchedule)
class GroomerScheduleAdmin(admin.ModelAdmin):
    list_display = ('groomer', 'monday_start', 'monday_end', 
    'tuesday_start', 'tuesday_end', 'wednesday_start', 'wednesday_end', 
    'thursday_start', 'thursday_end', 'friday_start', 'friday_end', 
    'saturday_start', 'saturday_end', 'sunday_start', 'sunday_end',
    'lunch_start', 'lunch_end',)
    search_fields = ['groomer']
