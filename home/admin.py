from django.contrib import admin
from .models import About, Services
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Services)
class ServicesAdmin(SummernoteModelAdmin):
    list_display = ('name', 'price', 'duration')
    search_fields = ['name']
    list_filter = ('price', 'duration',)
    summernote_fields = ('description',)


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('title', 'welcome_message')
    summernote_fields = ('content',)
