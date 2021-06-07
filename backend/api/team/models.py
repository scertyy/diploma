from django.db import models


class Team(models.Model):
    name = models.CharField(verbose_name='Название команды', max_length=256)
