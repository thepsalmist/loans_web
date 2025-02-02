from django.shortcuts import render, redirect
from django.contrib import messages


from .models import About, Testimonial, Faq, Contact
from .forms import ContactForm


def home(request):
    testimonials = Testimonial.objects.all()
    faqs = Faq.objects.all()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get("name")
            messages.success(request, f"Thank you {name} for contacting us")
            return redirect("core:home")
    else:
        form = ContactForm()

    context = {
        "testimonials": testimonials,
        "faqs": faqs,
        "form": form,
    }

    return render(request, "core/index.html", context)


def privacy(request):
    return render(request, "core/privacy.html", context={})
