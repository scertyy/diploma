from django.db import models


class Team(models.Model):
    name = models.CharField(verbose_name='Название команды', max_length=256)
    avatar = models.ImageField(null=True, upload_to='team_avatars', default='team_avatars/no_img.jpg')
    description = models.TextField(verbose_name='Описание команды', null=True)
    is_self = models.BooleanField(verbose_name='Единичная псевдокоманда для привязки Board к профилю', default=False)
    parent = models.ForeignKey('self', verbose_name='Подкоманда', related_name='sub_teams', null=True, on_delete=models.CASCADE)


class Position(models.Model):
    POSITION_CHOICES = (
        (1, 'creator'),
        (2, 'admin'),
        (3, 'project_manager'),
        (4, 'middle_contributor'),
        (5, 'junior_contributor'),
    )
    name = models.CharField(verbose_name='Название должности', max_length=128)
    position = models.CharField(verbose_name='Должность', choices=POSITION_CHOICES, max_length=128)


class Contributor(models.Model):
    profile = models.ForeignKey('profile.Profile', verbose_name='Участник команды', on_delete=models.CASCADE)
    team = models.ForeignKey(Team, verbose_name='Команда участника', related_name='contributors',
                             on_delete=models.CASCADE, null=True)
    position = models.ForeignKey(Position, verbose_name='Должность', on_delete=models.CASCADE)
