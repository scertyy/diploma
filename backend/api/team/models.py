from django.db import models


class Team(models.Model):
    name = models.CharField(verbose_name='Название команды', max_length=256)
    creator = models.ForeignKey('account.Profile', verbose_name='Создатель команды', on_delete=models.SET_NULL,
                                related_name='parent', null=True, blank=True)
    contributors = models.ManyToManyField('account.Profile', related_name='children',
                                          verbose_name='Список участников команды', blank=True)


class Project(models.Model):
    name = models.CharField(verbose_name='Название проекта', max_length=256)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    creator = models.ForeignKey('account.Profile', verbose_name='Создатель проекта', on_delete=models.SET_NULL,
                                null=True, blank=True)
