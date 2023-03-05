from django.utils import timezone
from datetime import datetime, timedelta
from django.dispatch import receiver
from listings.models import Pet
from .models import Medical_pet
from django.db.models.signals import post_save, pre_save,post_init

import os
import json


@receiver(post_save,sender=Pet)
def createPetMedical(sender,instance,created,**kwargs):
    with open(os.path.abspath(os.getcwd()) +'/static/assets/data/medical.json','r', encoding="utf8") as f:
        data = json.load(f)
    if created:
        if instance.dob is not None:
            if instance.age < 8:
                for i in data['Vaccinations']:
                    Medical_pet.objects.create(pet=instance, name = (i['name']), suggest_shot = instance.dob + timedelta(weeks =i['duration_pappy'][0]), dscription = (i['description']),symptoms =(i['symptoms']))
            if instance.age >= 8 and instance.age < 12:
                for i in data['Vaccinations']:
                    Medical_pet.objects.create(pet=instance, name = (i['name']), suggest_shot = instance.dob + timedelta(weeks =i['duration_pappy'][1]),dscription = (i['description']),symptoms =(i['symptoms']))   
            if instance.age >= 12 and instance.age < 52:
                for i in data['Vaccinations']:
                    Medical_pet.objects.create(pet=instance, name = (i['name']), suggest_shot = instance.dob + timedelta(weeks =i['duration_pappy'][2]),dscription = (i['description']),symptoms =(i['symptoms']))
            if instance.age > 52:
                for i in data['Vaccinations']:
                    Medical_pet.objects.create(pet=instance, name = (i['name']), dscription = (i['description']),symptoms =(i['symptoms']), shot_duration = i['duration_adult'] )


@receiver(pre_save,sender=Medical_pet)
def calc_date(instance, **kwargs):
    if instance.last_shot is not None:
      instance.next_shot = instance.last_shot + timedelta(weeks=instance.shot_duration)
    else: instance.next_shot = None

