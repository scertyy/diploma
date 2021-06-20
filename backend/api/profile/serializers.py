from rest_framework import serializers
from backend.api.profile.models import Profile
from backend.api.profile.services.serializers_utils import create_profile, add_instances_to_multiple_fields
from backend.api.team.serializers import TeamSerializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        """
        Переопределяем создание пользователя с дополнительным созданием профиля
        """
        return create_profile(validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'avatar', 'teams']
        depth = 1

    def update(self, instance, validated_data):
        """
        Переопределяем метод PATCH для правильного добавления инстансов в multiple поля модели
        """
        multiple_objects = ['teams']
        add_instances_to_multiple_fields(instance, multiple_objects, validated_data)
        return instance
