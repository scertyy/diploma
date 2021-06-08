from django.db import models


class Team(models.Model):
    name = models.CharField(verbose_name='Название команды', max_length=256)
    creator = models.ForeignKey('account.Profile', verbose_name='Создатель команды', on_delete=models.SET_NULL,
                                null=True, blank=True)
