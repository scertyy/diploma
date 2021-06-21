from backend.api.board.models import Board
from backend.api.profile.models import Profile
from backend.api.team.models import Team, Contributor, Position


def add_team_to_profile(validated_data, user):
    team = Team.objects.create(name=validated_data['name'])
    if validated_data.get('description'):
        team.description = validated_data['description']
    if validated_data.get('parent'):
        team.parent = validated_data['parent']
    team.save()
    if validated_data.get('contributors_for_create'):
        position, new = Position.objects.get_or_create(name='Участник', position=5)
        for contributor in validated_data['contributors_for_create']:
            Contributor.objects.create(team=team, profile_id=contributor, position=position)
    profile = Profile.objects.get(id=user.id)
    profile.teams.add(team)
    profile.save()
    position, new = Position.objects.get_or_create(name='Владелец', position=1)
    Contributor.objects.create(team=team, profile=profile, position=position)
    Board.objects.create(team=team, title='Резерв')
    Board.objects.create(team=team, title='План')
    Board.objects.create(team=team, title='В работе')
    Board.objects.create(team=team, title='Завершено')
    return team
