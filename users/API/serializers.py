from rest_framework import serializers
from users.models import Profile
from listings.models import Pet
from listings.API.serializers import PetSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    owner_pets = serializers.SerializerMethodField()
    
    def get_owner_pets(self,obj):
        listings = Pet.objects.filter(owner = obj.id)
        listings_serialezed = PetSerializer(listings, many=True)
        return listings_serialezed.data 
    class Meta:
        model = Profile
        fields="__all__"
    
      
