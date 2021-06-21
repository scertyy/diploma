from backend.api.profile.models import Profile
from backend.api.team.models import Team, Position, Contributor


def create_profile(validated_data):
    self_team = Team.objects.create(name='Мои задачи',
                                    avatar=None,
                                    is_self=True,
                                    parent=None)
    profile = Profile.objects.create_user(username=validated_data['username'],
                                          email=validated_data['email'],
                                          password=validated_data['password'],
                                          first_name=validated_data['first_name'],
                                          last_name=validated_data['last_name'])
    profile.teams.add(self_team)
    position, new = Position.objects.get_or_create(name='Владелец', position=1)
    Contributor.objects.create(profile=profile, team=self_team, position=position)
    return profile


def add_instances_to_multiple_fields(instance, multiple_objects, validated_data):
    for obj in multiple_objects:
        obj_list = validated_data.get(obj)
        if type(obj_list) == list:
            prof = getattr(instance, obj)
            prof.clear()
        if obj_list:
            prof = getattr(instance, obj)
            for obj_instance in obj_list:
                prof.add(obj_instance)
