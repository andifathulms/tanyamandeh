# Generated by Django 3.2 on 2021-08-29 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizTest', '0008_auto_20210823_0144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessionmark',
            name='quest88Ans',
        ),
        migrations.RemoveField(
            model_name='sessionmark',
            name='quest89Ans',
        ),
        migrations.RemoveField(
            model_name='sessionmark',
            name='quest90Ans',
        ),
        migrations.RemoveField(
            model_name='sessionmark',
            name='quest91Ans',
        ),
        migrations.RemoveField(
            model_name='sessionorder',
            name='quest88Pos',
        ),
        migrations.RemoveField(
            model_name='sessionorder',
            name='quest89Pos',
        ),
        migrations.RemoveField(
            model_name='sessionorder',
            name='quest90Pos',
        ),
        migrations.RemoveField(
            model_name='sessionorder',
            name='quest91Pos',
        ),
    ]
