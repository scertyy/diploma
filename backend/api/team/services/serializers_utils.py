from backend.api.profile.models import Profile
from backend.api.team.models import Team, Contributor


def add_team_to_profile(validated_data):
    team = Team.objects.create(**validated_data)
    team.contributors.add(team.creator.id)
    team.save()
    profile = Profile.objects.get(id=team.creator.id)
    profile.teams.add(team)
    profile.save()
    Contributor.objects.create(team=team, profile=profile, is_creator=True, position='Владелец')
    return team
