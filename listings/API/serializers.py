from rest_framework import serializers
from listings.models import Pet
from medical_pet_app.models import Medical_pet
from medical_pet_app.API.serializers import MedSerializer



class PetSerializer(serializers.ModelSerializer):
    pet_image1 = serializers.ImageField(required=False)
    pet_image2 = serializers.ImageField(required=False)
    pet_image3 = serializers.ImageField(required=False)
    pet_med = serializers.SerializerMethodField()
    def get_pet_med(self,obj):
        med_listing = Medical_pet.objects.filter(pet = obj.id)
        med_listing_serialized = MedSerializer(med_listing, many=True)
        return med_listing_serialized.data
    class Meta:
        model = Pet
        fields = '__all__'


class PetListingIDSerializer(serializers.ModelSerializer):
   
    class Meta:
        model =Pet
        fields = '__all__'
        depth = 1
        
        
