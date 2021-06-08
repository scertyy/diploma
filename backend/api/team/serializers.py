from rest_framework import serializers

from backend.api.profile.models import Profile
from backend.api.profile.serializers import ProfileSerializer
from backend.api.team.models import Team, Project
from backend.api.team.services.serializers_utils import add_team_to_profile


class TeamSerializer(serializers.ModelSerializer):
    count_of_contributors = serializers.SerializerMethodField('get_count_of_contributors')
    contributors = ProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = '__all__'

    def create(self, validated_data):
        """
        Переопределяем создание команды для добавления команды в профиль создателя
        """
        return add_team_to_profile(validated_data)

    def get_count_of_contributors(self, obj):
        return Profile.objects.filter(teams__in=[obj.id, ]).count()


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
