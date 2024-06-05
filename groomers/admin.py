from django.contrib import admin
from .models import Groomers

@admin.register(Groomers)
class GroomersAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']