from django.shortcuts import render
from .forms import ContactForm

def contact_request(request):
    contact_form = ContactForm()
    return render(
        request,
        "contact/contact_request.html",
        {
            "contact_form": contact_form,
            },
)
