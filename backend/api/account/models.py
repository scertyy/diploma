from django.contrib.auth.models import User
from django.db import models
from backend.api.team.models import Team


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь профиля', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Фото профиля', upload_to='profile_images/', null=True)
    teams = models.ManyToManyField(Team, verbose_name='Команды профиля', blank=True)
    position = models.CharField(verbose_name='Должность профиля', max_length=256, blank=True)
    majors = models.ManyToManyField('Profile', related_name='major', verbose_name='Начальники профиля', blank=True)
    minors = models.ManyToManyField('Profile', related_name='minor', verbose_name='Подчиненные профиля', blank=True)

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'
