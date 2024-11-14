from django import forms
from .models import Luma30, Luma07

class TabletForm(forms.ModelForm):
    class Meta:
        model = Luma30
        fields = '__all__'  # or specify specific fields

    class Meta:
        model = Luma07
        fields = '__all__'  # or specify specific fields    