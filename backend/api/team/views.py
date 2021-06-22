from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from backend.api.profile.models import Profile
from backend.api.team.models import Team, Contributor, Position
from backend.api.team.serializers import TeamSerializer, ContributorSerializer, PositionSerializer
from backend.api.team.services.views_utils import get_team_and_user_data


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.filter(parent=None)
    permission_classes = (permissions.IsAuthenticated, )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data={'success': 'deleted'})

    # ToDo: ПЕРЕПИСАТЬ
    @action(detail=False, methods=['post'], permission_classes=(permissions.IsAuthenticated, ))
    def add_contributor_to_team(self, request):
        """
        Добавляет пользователя(профиль) в команду
        """
        current_user = request.user
        profile_id, team_id = get_team_and_user_data(request)
        if not profile_id:
            return Response({'message': 'Передайте идентификатор добавляемого пользователя'})
        profile = Profile.objects.get(id=profile_id)
        team = Team.objects.get(id=team_id)
        if not team:
            return Response({'message': 'Команда с указанным идентификатором не найдена'})
        creator = Contributor.objects.get(team=team, profile=current_user)
        if creator.position != 1:
            return Response({'message': 'Вы не являетесь создателем указанной команды'})
        profile.teams.add(team)
        position = Position.objects.create(name='Участник', position=5)
        Contributor.objects.create(profile=profile, team=team, position=position)
        return Response({'success': 'Пользователь добавлен в команду'})

    @action(detail=False, methods=['post'], permission_classes=(permissions.IsAuthenticated, ))
    def delete_contributor_from_team(self, request):
        """
        Удаляет пользователя(профиль) из команды
        """
        contributor_id, team_id = get_team_and_user_data(request)
        if not contributor_id:
            return Response({'message': 'Передайте идентификатор удаляемого пользователя'})
        team = Team.objects.get(id=team_id)
        if not team:
            return Response({'message': 'Команда с указанным идентификатором не найдена'})
        contributor = Contributor.objects.get(id=contributor_id, team=team)
        if not contributor:
            return Response({'message': 'Пользователя с таким идентификатором не существует или '
                                        'данный пользователь не является участником указанной команды'})
        contributor.delete()
        return Response({'success': 'Пользователь удален из команды'})


class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ['team']


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
