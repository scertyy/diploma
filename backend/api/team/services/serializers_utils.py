from backend.api.account.models import Profile
from backend.api.team.models import Team


def add_team_to_profile(validated_data):
    team = Team.objects.create(**validated_data)
    profile = Profile.objects.get(id=team.creator.id)
    profile.teams.add(team)
    profile.save()
    return team