from django.shortcuts import render

from .models import About, Testimonial, Faq


def home(request):
    return render(request, "core/index.html", context={})
