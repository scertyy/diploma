from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response

from .models import Profile
from .serializers import RegisterSerializer, ProfileSerializer


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "success": "User Created Successfully.  Now perform Login to get your token",
            "profile_id": Profile.objects.get(user=user).id,
        })


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    # permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ['teams', 'user', 'position']
