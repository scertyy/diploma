import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Profile
from .serializers import RegisterSerializer, ProfileSerializer


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "success": "User Created Successfully. Now perform Login to get your token"
        })


class ProfileFilter(django_filters.FilterSet):
    teams = django_filters.CharFilter(field_name='teams', lookup_expr='in')

    class Meta:
        model = Profile
        fields = ['teams', 'user']


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, )
    filterset_class = ProfileFilter

    @action(detail=False, permission_classes=(permissions.IsAuthenticated,))
    def get_current_profile(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)
