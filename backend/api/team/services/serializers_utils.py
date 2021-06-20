from backend.api.board.models import Board
from backend.api.profile.models import Profile
from backend.api.team.models import Team, Contributor, Position


def add_team_to_profile(validated_data, user):
    team = Team.objects.create(**validated_data)
    profile = Profile.objects.get(id=user.id)
    profile.teams.add(team)
    profile.save()
    position = Position.objects.create(name='Владелец', position=1)
    Contributor.objects.create(team=team, profile=profile, position=position)
    Board.objects.create(team=team, title='Резерв')
    Board.objects.create(team=team, title='План')
    Board.objects.create(team=team, title='В работе')
    Board.objects.create(team=team, title='Завершено')
    return team
