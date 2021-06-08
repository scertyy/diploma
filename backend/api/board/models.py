from django.db import models
from django.db.models import Max

from backend.api.profile.models import Profile
from backend.api.team.models import Project


class Board(models.Model):
    project = models.ForeignKey(Project, verbose_name='Проект', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название доски', max_length=256)
    position = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)

    def save(self, *args, **kwargs):
        filtered_objects = Board.objects.filter(project=self.project)
        if not self.position and filtered_objects.count() == 0:
            self.position = 2 ** 16 - 1
        elif not self.position:
            self.position = filtered_objects.aggregate(Max('position'))[
                'position__max'] + 2 ** 16 - 1
        return super().save(*args, **kwargs)


class Task(models.Model):
    board = models.ForeignKey(Board, verbose_name='Доска задачи', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название задачи', max_length=256)
    text = models.TextField(verbose_name='Текст задачи')
    color = models.CharField(verbose_name='Цвет задачи', max_length=256)
    deadline = models.DateTimeField('Время выполнения')
    position = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    created = models.DateTimeField("Created", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Updated", auto_now_add=False, auto_now=True)

    def save(self, *args, **kwargs):
        filtered_objects = Task.objects.filter(board=self.board)
        if not self.position and filtered_objects.count() == 0:
            self.position = 2 ** 16 - 1
        elif not self.position:
            self.position = filtered_objects.aggregate(Max('position'))[
                'position__max'] + 2 ** 16 - 1
        return super().save(*args, **kwargs)


class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField("Created", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Updated", auto_now_add=False, auto_now=True)

