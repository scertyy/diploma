from rest_framework import serializers
from django.contrib.auth.models import User

from backend.api.account.models import Profile
from backend.api.account.services.serializers_utils import create_user_and_profile, add_instances_to_multiple_fields


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        """
        Переопределяем создание пользователя с дополнительным созданием профиля
        """
        return create_user_and_profile(validated_data)


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
        """
        Переопределяем метод PATCH для правильного добавления инстансов в multiple поля модели
        """
        multiple_objects = ['teams', 'majors', 'minors']
        add_instances_to_multiple_fields(instance, multiple_objects, validated_data)
        return instance
