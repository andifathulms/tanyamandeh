# Generated by Django 3.2 on 2021-09-01 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizTest', '0010_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='responden',
            name='nohp',
            field=models.CharField(default=1111111111, max_length=20),
            preserve_default=False,
        ),
    ]