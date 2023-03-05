from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Pet
from medical_pet_app.models import Medical_pet
from datetime import datetime
import datetime


@receiver(pre_save, sender=Pet)
def calculate_age(sender, instance, **kwargs):
    today = datetime.date.today()
    if instance.dob is not None:
        age_seconds = (today - instance.dob).total_seconds()
        age_weeks = age_seconds /604800
        round_weeks = float('%.2f' % age_weeks)
        print(type(round_weeks))
        instance.age = round_weeks





