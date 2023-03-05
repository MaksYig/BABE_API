from  models import Medical_pet
from .serializers import MedSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.dispatch import receiver


