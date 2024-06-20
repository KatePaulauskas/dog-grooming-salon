from django.urls import path
from .views import book_appointment_step_one

urlpatterns = [
    path('',  book_appointment_step_one, name='book_appointment_step_one'),
]