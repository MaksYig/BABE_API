from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
#User = get_user_model()
# Create your models here.
class User(AbstractUser):
    email= models.EmailField(unique=True)
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    f_name = models.CharField('First Name',max_length=20,null=True, blank=True)
    l_name = models.CharField('Last Name',max_length=20,null=True, blank=True)
    phone = models.CharField('Phone',max_length=20,null=True, blank=True)
    country = models.CharField('Country',max_length=100,null=True,blank=True)
    city = models.CharField('City',max_length=100,null=True,blank=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='profile_pictures/%Y/%m/%d',default='default_user.png')
    
    def __str__(self):
        return f'{self.user}'