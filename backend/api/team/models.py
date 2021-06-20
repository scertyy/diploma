from django.db import models


class Team(models.Model):
    name = models.CharField(verbose_name='Название команды', max_length=256)
    creator = models.ForeignKey('profile.Profile', verbose_name='Создатель команды', on_delete=models.SET_NULL,
                                related_name='parent', null=True, blank=True)
    contributors = models.ManyToManyField('profile.Profile', related_name='children',
                                          verbose_name='Список участников команды', blank=True)
# ToDo: При создании команды, создается 4 Board привязанных к ней с именами Резерв, К выполнению, В работе, Завершено


class Contributor(models.Model):
    profile = models.ForeignKey('profile.Profile', verbose_name='Участник команды', on_delete=models.CASCADE)
    team = models.ForeignKey(Team, verbose_name='Команда участника', on_delete=models.CASCADE)
    position = models.CharField(verbose_name='Должность', max_length=256)
    is_creator = models.BooleanField(verbose_name='Является ли создателем команды')


class Project(models.Model):
    name = models.CharField(verbose_name='Название проекта', max_length=256)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    creator = models.ForeignKey('profile.Profile', verbose_name='Создатель проекта', on_delete=models.SET_NULL,
                                null=True, blank=True)
