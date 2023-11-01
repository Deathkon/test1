from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'subject', 'email', 'phone', 'message']
