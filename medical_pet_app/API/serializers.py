from rest_framework import serializers
from medical_pet_app.models import Medical_pet

class MedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical_pet
        fields = '__all__'
