from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Gallery


def gallery(request):
    galleries = Gallery.objects.all().order_by('-updated_on')
    # Show 6 images per page.
    paginator = Paginator(galleries, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "gallery/gallery.html",
        {
            "page_obj": page_obj,
            "is_paginated": page_obj.has_other_pages(),
        }
    )
