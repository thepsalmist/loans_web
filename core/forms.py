from django import forms
from phonenumber_field.formfields import PhoneNumberField

from .models import Contact


class ContactForm(forms.ModelForm):
    phone_number = PhoneNumberField()

    class Meta:
        model = Contact
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name"}),
            "email": forms.TextInput(attrs={"placeholder": "Email"}),
            "message": forms.Textarea(attrs={"placeholder": "Message..."}),
        }
