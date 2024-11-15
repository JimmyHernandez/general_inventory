from django import forms
from .models import Tabletas, Departamento

class FormTableta(forms.ModelForm):
    class Meta:
        model = Tabletas
        fields = '__all__'  # or specify specific fields

class FormDepartamento(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'  # or specify specific fields

  