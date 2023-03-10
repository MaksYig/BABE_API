from .serializers import MedSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.dispatch import receiver
from medical_pet_app.models import Medical_pet

class UpdateMed(generics.UpdateAPIView):
    queryset = Medical_pet.objects.all()
    serializer_class = MedSerializer
    # permission_classes=[IsAuthenticated]
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():   
            serializer.save()
            return Response({"message": "Your medical information was updated successfully!",
                             "data": serializer.data
                             })
        else:
            return Response({"message": "failed", "details": serializer.errors})  

