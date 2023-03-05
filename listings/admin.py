from django.contrib import admin
from listings.models import Pet
from .forms import PetForm

# Register your models here.
class PetAdmin(admin.ModelAdmin):
    form = PetForm


admin.site.register(Pet, PetAdmin)
