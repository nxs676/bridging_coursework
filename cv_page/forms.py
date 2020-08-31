from django import forms
from .models import CV


class CVForm(forms.ModelForm):

    class Meta:
        model = CV
        fields = ('address', 'phone', 'email', 'summary', 'skills', 'education', 'jobs')

