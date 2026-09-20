from django import forms

from .models import Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['site_url', 'password']
        labels = {
            'site_url': 'Website URL',
            'password': 'Password',
        }