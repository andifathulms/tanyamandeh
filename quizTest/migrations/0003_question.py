# Generated by Django 3.2 on 2021-07-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizTest', '0002_wilayah'),
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionID', models.IntegerField()),
                ('question', models.TextField()),
                ('category', models.CharField(max_length=200)),
                ('option1', models.TextField()),
                ('option2', models.TextField()),
                ('option3', models.TextField()),
                ('option4', models.TextField()),
                ('chooseOption1', models.IntegerField()),
                ('chooseOption2', models.IntegerField()),
                ('chooseOption3', models.IntegerField()),
                ('chooseOption4', models.IntegerField()),
            ],
        ),
    ]
