from django import forms
from .models import Medical_pet

class MedForm(forms.ModelForm):
    class Meta:
        model = Medical_pet
        fields = '__all__'

