from django.urls import path
from .views import book_appointment_step_one,  book_appointment_step_two

urlpatterns = [
    path('',  book_appointment_step_one, name='book_appointment_step_one'),
    path('time/', book_appointment_step_two, name='book_appointment_step_two'),
]