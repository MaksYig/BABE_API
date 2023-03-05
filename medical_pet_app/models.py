from django.db import models
from random import choices
from django.utils import timezone


# Create your models here.
class Medical_pet(models.Model):
    pet = models.ForeignKey(to = 'listings.Pet',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dscription = models.TextField(blank=True,null=True)
    symptoms = models.TextField(blank=True,null=True)
    suggest_shot = models.DateField(null=True, blank=True)
    last_shot = models.DateField(null=True, blank=True)
    next_shot = models.DateField(null=True, blank=True)
    notification = models.BooleanField(default=False)
    shot_duration = models.IntegerField('Shot duration in weeks',null=True, blank=True)
    is_adult = models.BooleanField(default=True)

    def __str__(self):
        return f'Medical for {self.pet.name} {self.name}'
