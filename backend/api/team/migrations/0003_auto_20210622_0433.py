# Generated by Django 3.1.12 on 2021-06-21 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20210621_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='avatar',
            field=models.ImageField(default='team_avatars/no_img.jpg', null=True, upload_to='team_avatars'),
        ),
    ]