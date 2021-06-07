from rest_framework import viewsets, permissions

from backend.api.team.models import Team
from backend.api.team.serializers import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    # permission_classes = (permissions.IsAuthenticated, )
