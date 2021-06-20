from django.contrib.auth.models import User, AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from backend.api.team.models import Team

username_validator = RegexValidator(
    r'^[a-zA-Z0-9_\.]*$', 'Only alphanumeric characters, underscores, and periods are allowed in your username.')


class Profile(AbstractUser):
    username = models.CharField(
        max_length=15, blank=False, null=False, unique=True, validators=[username_validator])
    email = models.EmailField(
        max_length=255, blank=False, null=False, unique=True)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    avatar = models.ImageField(blank=True, upload_to='profile_avatars', default='profile_avatars/no_img.jpg')
    teams = models.ManyToManyField(Team, verbose_name='Команды профиля')
    level = models.PositiveIntegerField(verbose_name='Уровень профиля', default=1)
    experience = models.PositiveIntegerField(verbose_name='Количество опыта в текущем уровне', default=0)
    experience_in_level = models.PositiveIntegerField(verbose_name='Количество опыта в уровне', default=1000)

    def __str__(self):
        return f'Профиль пользователя {self.username}'
