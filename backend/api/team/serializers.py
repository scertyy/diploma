from rest_framework import serializers

from backend.api.account.models import Profile
from backend.api.team.models import Team


class TeamSerializer(serializers.ModelSerializer):
    count_of_contributors = serializers.SerializerMethodField('get_count_of_contributors')

    class Meta:
        model = Team
        fields = '__all__'

    def create(self, validated_data):
        team = Team.objects.create(**validated_data)
        profile = Profile.objects.get(id=team.creator.id)
        profile.teams.add(team)
        profile.save()
        return team

    def get_count_of_contributors(self, obj):
        count = Profile.objects.filter(teams__in=[obj.id, ]).count()
        return count
