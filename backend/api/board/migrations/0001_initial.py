# Generated by Django 3.1.12 on 2021-06-08 23:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название доски')),
                ('position', models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.project', verbose_name='Проект')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название задачи')),
                ('text', models.TextField(verbose_name='Текст задачи')),
                ('color', models.CharField(max_length=256, verbose_name='Цвет задачи')),
                ('deadline', models.DateTimeField(verbose_name='Время выполнения')),
                ('position', models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.board', verbose_name='Доска задачи')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.task')),
            ],
        ),
    ]
