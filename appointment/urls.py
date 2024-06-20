from django.urls import path
from .views import book_appointment_step_one,  book_appointment_step_two, my_appointments

urlpatterns = [
    path('',  book_appointment_step_one, name='book_appointment_step_one'),
    path('time/', book_appointment_step_two, name='book_appointment_step_two'),
    path('my-appointments/', my_appointments, name='my_appointments'),
]