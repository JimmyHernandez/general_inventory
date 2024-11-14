from django import forms
from .models import Luma07

class FormLuma07(forms.ModelForm):
    class Meta:
        model = Luma07
        fields = '__all__'  # or specify specific fields

  