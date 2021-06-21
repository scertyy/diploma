from rest_framework import serializers

from backend.api.profile.models import Profile
from backend.api.team.models import Team, Contributor, Position
from backend.api.team.services.serializers_utils import add_team_to_profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'avatar', 'level', 'experience', 'experience_in_level']


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class ContributorSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    position = PositionSerializer()

    class Meta:
        model = Contributor
        fields = '__all__'


class SubTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    contributors = ContributorSerializer(many=True, read_only=True)
    sub_teams = SubTeamSerializer(many=True, read_only=True)
    contributors_for_create = serializers.ListField(write_only=True, required=False)

    class Meta:
        model = Team
        fields = '__all__'

    def create(self, validated_data):
        """
        Переопределяем создание команды для добавления команды в профиль создателя
        """
        return add_team_to_profile(validated_data, self.context.get('request').user)
