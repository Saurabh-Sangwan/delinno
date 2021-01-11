from django import forms
from .models import Contact
from django.forms import ModelForm

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name','email','message']
    