from rest_framework import serializers

from backend.api.account.models import Profile
from backend.api.team.models import Team
from backend.api.team.services.serializers_utils import add_team_to_profile


class TeamSerializer(serializers.ModelSerializer):
    count_of_contributors = serializers.SerializerMethodField('get_count_of_contributors')

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
