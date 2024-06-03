from django.views.generic import ListView
from .models import About, Services

class HomeView(ListView):
    model = Services
    template_name = 'home/index.html'
    context_object_name = 'services_list'

    # Use the get_context_data method to include multiple models' data in a Django class-based view
    # https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/#adding-extra-context
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the About model data above services list
        context['about'] = About.objects.first()
        return context