from django.shortcuts import render
from .models import Groomers


def groomers(request):
    groomers = Groomers.objects.all().order_by('-updated_on')

    return render(
        request,
        "groomers/groomers.html",
        {"groomers": groomers},
    )
