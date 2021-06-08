from rest_framework import serializers
from django.contrib.auth.models import User

from backend.api.account.models import Profile


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],
                                        email=validated_data['email'],
                                        password=validated_data['password'],
                                        first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'])
        profile = Profile.objects.create(user=user)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def update(self, instance, validated_data):
        profile = instance
        multiple = ['teams', 'majors', 'minors']
        for obj in multiple:
            obj_list = validated_data.get(obj)
            if type(obj_list) == list:
                prof = getattr(profile, obj)
                prof.clear()
            if obj_list:
                prof = getattr(profile, obj)
                for obj_instance in obj_list:
                    prof.add(obj_instance)
        return profile
