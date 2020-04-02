from django.contrib import admin

from .models import Testimonial, About, Contact, Faq


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["client_name", "client_title", "message"]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "message", "publish_date"]


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ["title", "body"]


admin.site.register(About)
