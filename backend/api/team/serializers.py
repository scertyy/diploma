from rest_framework import serializers

from backend.api.team.models import Team, Contributor
from backend.api.team.services.serializers_utils import add_team_to_profile


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'


class SubTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    contributors = ContributorSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = '__all__'

    def create(self, validated_data):
        """
        Переопределяем создание команды для добавления команды в профиль создателя
        """
        return add_team_to_profile(validated_data, self.context.get('request').user)
