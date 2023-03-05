from users.models import Profile
from .serializers import ProfileSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class ProfileDetails(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes=[IsAuthenticated]
    lookup_field = 'user'


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=[IsAuthenticated]
    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)

class UserProfileUpdateView(generics.UpdateAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=[IsAuthenticated]
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():   
            serializer.save()
            return Response({"message": "User was updated successfully!",
                             "data": serializer.data
                             })
        else:
            return Response({"message": "failed", "details": serializer.errors}) 