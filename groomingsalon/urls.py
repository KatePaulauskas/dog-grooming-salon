from django.contrib import admin
from django.urls import path, include
from groomingsalon.views import handler404, handler500
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('appointment/', include('appointment.urls'), name='appointment_urls'),
    path('contact/', include('contact_request.urls'), name='contact_urls'),
    path('gallery/', include('gallery.urls'), name='gallery_urls'),
    path('groomers/', include('groomers.urls'), name='groomers_urls'),
    path('summernote/', include('django_summernote.urls')),
    path('', include('home.urls'), name='home-urls'),
]

# Error handlers
handler404 = 'groomingsalon.views.handler404'
handler500 = 'groomingsalon.views.handler500'
