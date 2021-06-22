from datetime import datetime

import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Profile
from .serializers import RegisterSerializer, ProfileSerializer
from ..board.models import Task
from ..team.models import Contributor


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
        fields = ['teams']


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_class = ProfileFilter
    search_fields = ['username']

    @action(detail=False, permission_classes=(permissions.IsAuthenticated,))
    def get_current_profile(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @action(detail=False, permission_classes=(permissions.IsAuthenticated,))
    def get_profile_statistics(self, request):
        profile = request.user
        teams = profile.teams.all().filter(is_self=False)
        all_profile_contributors = Contributor.objects.filter(profile=profile, team__in=teams)
        plan = Task.objects.filter(contributor__in=all_profile_contributors, board__title='План').count()
        doing = Task.objects.filter(contributor__in=all_profile_contributors, board__title='В работе').count()
        deadline = Task.objects.filter(contributor__in=all_profile_contributors, deadline__day=datetime.today().day).count()
        done = Task.objects.filter(contributor__in=all_profile_contributors, board__title='Завершено').count()
        done_today = Task.objects.filter(contributor__in=all_profile_contributors,
                                         when_completed__day=datetime.today().day, board__title='Завершено').count()
        done_for_week = Task.objects.filter(contributor__in=all_profile_contributors,
                                            when_completed__day__gte=datetime.today().day-7,
                                            board__title='Завершено').count()
        return Response(data={'plan': plan, 'doing': doing, 'deadline': deadline, 'done': done,
                              'done_today': done_today, 'done_for_week': done_for_week})
