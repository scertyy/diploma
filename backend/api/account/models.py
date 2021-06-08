from django.contrib.auth.models import User
from django.db import models
from backend.api.team.models import Team


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь профиля', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Фото профиля', upload_to='profile_images/', null=True)
    teams = models.ManyToManyField(Team, verbose_name='Команды профиля', blank=True)

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'
