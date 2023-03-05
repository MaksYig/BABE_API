from .serializers import PetSerializer
from .serializers import PetListingIDSerializer
import json
from rest_framework.response import Response
from rest_framework import status
from listings.models import Pet
from rest_framework import generics
from rest_framework.views import APIView
from users.models import Profile
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class ListingPets(generics.ListAPIView):
    queryset = Pet.objects.all() 
    serializer_class = PetSerializer

class PetListingID(APIView):
    def get(self, request, id):
        pet = Pet.objects.get(id=id)
        if not pet:
            return Response(
                {"res": "Object with tpet id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = PetListingIDSerializer(pet)
        return Response({"message":"Successfull got pet information", "data":serializer.data},status=status.HTTP_200_OK)

class CreatePets(generics.CreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes=[IsAuthenticated]
    

class UpdatePet(generics.UpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes=[IsAuthenticated]
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():   
            serializer.save()
            return Response({"message": "Your pet info was updated successfully!",
                             "data": serializer.data
                             })
        else:
            return Response({"message": "failed", "details": serializer.errors}) 
        
class DeletePets(generics.DestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes=[IsAuthenticated]
    lookup_field = 'id'
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_destroy(instance)
            return Response({"message": "Your pet was deleted successfully",
                             "data": serializer.data
                             },status=status.HTTP_200_OK)
        else:
            return Response({"message": "failed", "details": serializer.errors}) 
        

