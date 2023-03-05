from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name','age','pet_breed','chip_num','pet_gender','dob','pet_color','pet_disc','owner','created_at','pet_image1','pet_image2','pet_image3']
