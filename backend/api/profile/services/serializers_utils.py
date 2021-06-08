from backend.api.profile.models import Profile


def create_profile(validated_data):
    profile = Profile.objects.create_user(username=validated_data['username'],
                                       email=validated_data['email'],
                                       password=validated_data['password'],
                                       first_name=validated_data['first_name'],
                                       last_name=validated_data['last_name'])
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
