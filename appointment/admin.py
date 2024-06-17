from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'groomer', 'date', 'time', 'status')
    search_fields = ['user__username', 'service__name', 'groomer__name']
    list_filter = ('status', 'groomer', 'service', 'date',)