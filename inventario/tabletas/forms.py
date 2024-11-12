from django import forms
from .models import NewTablet

class TabletForm(forms.ModelForm):
    class Meta:
        model = NewTablet
        fields = '__all__'  # or specify specific fields