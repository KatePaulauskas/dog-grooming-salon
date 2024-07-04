from django.views.generic import ListView
from .models import About, Services
from django.shortcuts import render
from django.shortcuts import render

def test_error(request):
    """
    View that deliberately raises an exception to test 500 error page.
    """
    raise Exception("This is a test 500 error!")

class HomeView(ListView):
    model = Services
    template_name = 'home/index.html'
    context_object_name = 'services_list'

    def get_queryset(self):
        # Order services by 'position'
        return Services.objects.all().order_by('position')

    """
    Use the get_context_data method to include multiple models' data
    in a Django class-based view
    Source: Django Documentation - Adding extra context
    """
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the About model data above services list
        context['about'] = About.objects.first()
        return context
