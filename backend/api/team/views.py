from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from backend.api.profile.models import Profile
from backend.api.team.models import Team, Contributor
from backend.api.team.serializers import TeamSerializer, ContributorSerializer
from backend.api.team.services.views_utils import get_team_and_user_data


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    permission_classes = (permissions.IsAuthenticated, )

    # ToDo: ПЕРЕПИСАТЬ
    @action(detail=False, methods=['post'], permission_classes=(permissions.IsAuthenticated, ))
    def add_contributor_to_team(self, request):
        """
        Добавляет пользователя(профиль) в команду
        """
        current_user = request.user
        profile_id, team_id, position = get_team_and_user_data(request)
        if not profile_id:
            return Response({'message': 'Передайте идентификатор добавляемого пользователя'})
        profile = Profile.objects.get(id=profile_id)
        team = Team.objects.get(id=team_id)
        if not team:
            return Response({'message': 'Команда с указанным идентификатором не найдена'})
        if team.creator != current_user:
            return Response({'message': 'Вы не являетесь создателем указанной команды'})
        profile.teams.add(team)
        team.contributors.add(profile)
        Contributor.objects.create(profile=profile, team=team, position=position, is_creator=False)
        return Response({'success': 'Пользователь добавлен в команду'})

    @action(detail=False, methods=['post'], permission_classes=(permissions.IsAuthenticated, ))
    def delete_contributor_from_team(self, request):
        """
        Удаляет пользователя(профиль) из команды
        """
        profile_id, team_id = get_team_and_user_data(request)
        if not profile_id:
            return Response({'message': 'Передайте идентификатор удаляемого пользователя'})
        profile = Profile.objects.get(id=profile_id)
        team = Team.objects.get(id=team_id)
        if not team:
            return Response({'message': 'Команда с указанным идентификатором не найдена'})
        if team not in profile.teams.all():
            return Response({'message': 'Данный пользователь не является участником указанной команды'})
        profile.teams.remove(team)
        team.contributors.remove(profile)
        contributor = Contributor.objects.get(profile=profile, team=team, is_creator=False)
        contributor.delete()
        return Response({'success': 'Пользователь удален из команды'})


class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ['team']
