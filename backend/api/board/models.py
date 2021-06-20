from django.db import models
from django.db.models import Max

from backend.api.profile.models import Profile
from backend.api.team.models import Team, Contributor


class Board(models.Model):
    team = models.ForeignKey(Team, verbose_name='Проект', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название доски', max_length=256)
    priority = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    def save(self, *args, **kwargs):
        filtered_objects = Board.objects.filter(team=self.team)
        if not self.priority and filtered_objects.count() == 0:
            self.priority = 2 ** 16 - 1
        elif not self.priority:
            self.priority = filtered_objects.aggregate(Max('priority'))[
                'priority__max'] + 2 ** 16 - 1
        return super().save(*args, **kwargs)


class Task(models.Model):
    DIFFICULTY_CHOICES = (
        (50, 'easy'),
        (100, 'medium'),
        (200, 'hard')
    )
    board = models.ForeignKey(Board, verbose_name='Доска задачи', related_name='tasks', on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, verbose_name='Исполнитель задачи', null=True, on_delete=models.SET_NULL)
    title = models.CharField(verbose_name='Название задачи', max_length=256)
    description = models.TextField(verbose_name='Описание задачи')
    color = models.CharField(verbose_name='Цвет задачи', max_length=256)
    deadline = models.DateTimeField('Время выполнения')
    priority = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    difficulty = models.CharField(verbose_name='Сложность задачи', choices=DIFFICULTY_CHOICES, max_length=128)
    is_completed = models.BooleanField(verbose_name='Выполнена ли задача')
    parent = models.ForeignKey('self', verbose_name='Подзадача', on_delete=models.CASCADE)
    created = models.DateTimeField("Created", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Updated", auto_now_add=False, auto_now=True)

    def save(self, *args, **kwargs):
        filtered_objects = Task.objects.filter(board=self.board)
        if not self.priority and filtered_objects.count() == 0:
            self.priority = 2 ** 16 - 1
        elif not self.priority:
            self.priority = filtered_objects.aggregate(Max('priority'))[
                'priority__max'] + 2 ** 16 - 1
        return super().save(*args, **kwargs)


class Comment(models.Model):
    contributor = models.ForeignKey(Contributor, on_delete=models.SET_NULL, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField("Created", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Updated", auto_now_add=False, auto_now=True)

