
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Profile
from django.db.models.signals import post_save
User = get_user_model()

@receiver(post_save,sender=User)
def createUserProfile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def saveUserProfile(sender,instance,**kwargs):
    instance.profile.save()