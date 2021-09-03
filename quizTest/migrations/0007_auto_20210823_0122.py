# Generated by Django 3.2 on 2021-08-22 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizTest', '0006_auto_20210822_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='sessionMark',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('quest1Ans', models.IntegerField()),
                ('quest2Ans', models.IntegerField()),
                ('quest3Ans', models.IntegerField()),
                ('quest4Ans', models.IntegerField()),
                ('quest5Ans', models.IntegerField()),
                ('quest6Ans', models.IntegerField()),
                ('quest7Ans', models.IntegerField()),
                ('quest8Ans', models.IntegerField()),
                ('quest9Ans', models.IntegerField()),
                ('quest10Ans', models.IntegerField()),
                ('quest11Ans', models.IntegerField()),
                ('quest12Ans', models.IntegerField()),
                ('quest13Ans', models.IntegerField()),
                ('quest14Ans', models.IntegerField()),
                ('quest15Ans', models.IntegerField()),
                ('quest16Ans', models.IntegerField()),
                ('quest17Ans', models.IntegerField()),
                ('quest18Ans', models.IntegerField()),
                ('quest19Ans', models.IntegerField()),
                ('quest20Ans', models.IntegerField()),
                ('quest21Ans', models.IntegerField()),
                ('quest22Ans', models.IntegerField()),
                ('quest23Ans', models.IntegerField()),
                ('quest24Ans', models.IntegerField()),
                ('quest25Ans', models.IntegerField()),
                ('quest26Ans', models.IntegerField()),
                ('quest27Ans', models.IntegerField()),
                ('quest28Ans', models.IntegerField()),
                ('quest29Ans', models.IntegerField()),
                ('quest30Ans', models.IntegerField()),
                ('quest31Ans', models.IntegerField()),
                ('quest32Ans', models.IntegerField()),
                ('quest33Ans', models.IntegerField()),
                ('quest34Ans', models.IntegerField()),
                ('quest35Ans', models.IntegerField()),
                ('quest36Ans', models.IntegerField()),
                ('quest37Ans', models.IntegerField()),
                ('quest38Ans', models.IntegerField()),
                ('quest39Ans', models.IntegerField()),
                ('quest40Ans', models.IntegerField()),
                ('quest41Ans', models.IntegerField()),
                ('quest42Ans', models.IntegerField()),
                ('quest43Ans', models.IntegerField()),
                ('quest44Ans', models.IntegerField()),
                ('quest45Ans', models.IntegerField()),
                ('quest46Ans', models.IntegerField()),
                ('quest47Ans', models.IntegerField()),
                ('quest48Ans', models.IntegerField()),
                ('quest49Ans', models.IntegerField()),
                ('quest50Ans', models.IntegerField()),
                ('quest51Ans', models.IntegerField()),
                ('quest52Ans', models.IntegerField()),
                ('quest53Ans', models.IntegerField()),
                ('quest54Ans', models.IntegerField()),
                ('quest55Ans', models.IntegerField()),
                ('quest56Ans', models.IntegerField()),
                ('quest57Ans', models.IntegerField()),
                ('quest58Ans', models.IntegerField()),
                ('quest59Ans', models.IntegerField()),
                ('quest60Ans', models.IntegerField()),
                ('quest61Ans', models.IntegerField()),
                ('quest62Ans', models.IntegerField()),
                ('quest63Ans', models.IntegerField()),
                ('quest64Ans', models.IntegerField()),
                ('quest65Ans', models.IntegerField()),
                ('quest66Ans', models.IntegerField()),
                ('quest67Ans', models.IntegerField()),
                ('quest68Ans', models.IntegerField()),
                ('quest69Ans', models.IntegerField()),
                ('quest71Ans', models.IntegerField()),
                ('quest72Ans', models.IntegerField()),
                ('quest73Ans', models.IntegerField()),
                ('quest74Ans', models.IntegerField()),
                ('quest75Ans', models.IntegerField()),
                ('quest76Ans', models.IntegerField()),
                ('quest77Ans', models.IntegerField()),
                ('quest78Ans', models.IntegerField()),
                ('quest79Ans', models.IntegerField()),
                ('quest70Ans', models.IntegerField()),
                ('quest81Ans', models.IntegerField()),
                ('quest82Ans', models.IntegerField()),
                ('quest83Ans', models.IntegerField()),
                ('quest84Ans', models.IntegerField()),
                ('quest85Ans', models.IntegerField()),
                ('quest86Ans', models.IntegerField()),
                ('quest87Ans', models.IntegerField()),
                ('quest88Ans', models.IntegerField()),
                ('quest89Ans', models.IntegerField()),
                ('quest90Ans', models.IntegerField()),
                ('quest91Ans', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='sessionOrder',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('quest1Pos', models.IntegerField()),
                ('quest2Pos', models.IntegerField()),
                ('quest3Pos', models.IntegerField()),
                ('quest4Pos', models.IntegerField()),
                ('quest5Pos', models.IntegerField()),
                ('quest6Pos', models.IntegerField()),
                ('quest7Pos', models.IntegerField()),
                ('quest8Pos', models.IntegerField()),
                ('quest9Pos', models.IntegerField()),
                ('quest10Pos', models.IntegerField()),
                ('quest11Pos', models.IntegerField()),
                ('quest12Pos', models.IntegerField()),
                ('quest13Pos', models.IntegerField()),
                ('quest14Pos', models.IntegerField()),
                ('quest15Pos', models.IntegerField()),
                ('quest16Pos', models.IntegerField()),
                ('quest17Pos', models.IntegerField()),
                ('quest18Pos', models.IntegerField()),
                ('quest19Pos', models.IntegerField()),
                ('quest20Pos', models.IntegerField()),
                ('quest21Pos', models.IntegerField()),
                ('quest22Pos', models.IntegerField()),
                ('quest23Pos', models.IntegerField()),
                ('quest24Pos', models.IntegerField()),
                ('quest25Pos', models.IntegerField()),
                ('quest26Pos', models.IntegerField()),
                ('quest27Pos', models.IntegerField()),
                ('quest28Pos', models.IntegerField()),
                ('quest29Pos', models.IntegerField()),
                ('quest30Pos', models.IntegerField()),
                ('quest31Pos', models.IntegerField()),
                ('quest32Pos', models.IntegerField()),
                ('quest33Pos', models.IntegerField()),
                ('quest34Pos', models.IntegerField()),
                ('quest35Pos', models.IntegerField()),
                ('quest36Pos', models.IntegerField()),
                ('quest37Pos', models.IntegerField()),
                ('quest38Pos', models.IntegerField()),
                ('quest39Pos', models.IntegerField()),
                ('quest40Pos', models.IntegerField()),
                ('quest41Pos', models.IntegerField()),
                ('quest42Pos', models.IntegerField()),
                ('quest43Pos', models.IntegerField()),
                ('quest44Pos', models.IntegerField()),
                ('quest45Pos', models.IntegerField()),
                ('quest46Pos', models.IntegerField()),
                ('quest47Pos', models.IntegerField()),
                ('quest48Pos', models.IntegerField()),
                ('quest49Pos', models.IntegerField()),
                ('quest50Pos', models.IntegerField()),
                ('quest51Pos', models.IntegerField()),
                ('quest52Pos', models.IntegerField()),
                ('quest53Pos', models.IntegerField()),
                ('quest54Pos', models.IntegerField()),
                ('quest55Pos', models.IntegerField()),
                ('quest56Pos', models.IntegerField()),
                ('quest57Pos', models.IntegerField()),
                ('quest58Pos', models.IntegerField()),
                ('quest59Pos', models.IntegerField()),
                ('quest60Pos', models.IntegerField()),
                ('quest61Pos', models.IntegerField()),
                ('quest62Pos', models.IntegerField()),
                ('quest63Pos', models.IntegerField()),
                ('quest64Pos', models.IntegerField()),
                ('quest65Pos', models.IntegerField()),
                ('quest66Pos', models.IntegerField()),
                ('quest67Pos', models.IntegerField()),
                ('quest68Pos', models.IntegerField()),
                ('quest69Pos', models.IntegerField()),
                ('quest71Pos', models.IntegerField()),
                ('quest72Pos', models.IntegerField()),
                ('quest73Pos', models.IntegerField()),
                ('quest74Pos', models.IntegerField()),
                ('quest75Pos', models.IntegerField()),
                ('quest76Pos', models.IntegerField()),
                ('quest77Pos', models.IntegerField()),
                ('quest78Pos', models.IntegerField()),
                ('quest79Pos', models.IntegerField()),
                ('quest70Pos', models.IntegerField()),
                ('quest81Pos', models.IntegerField()),
                ('quest82Pos', models.IntegerField()),
                ('quest83Pos', models.IntegerField()),
                ('quest84Pos', models.IntegerField()),
                ('quest85Pos', models.IntegerField()),
                ('quest86Pos', models.IntegerField()),
                ('quest87Pos', models.IntegerField()),
                ('quest88Pos', models.IntegerField()),
                ('quest89Pos', models.IntegerField()),
                ('quest90Pos', models.IntegerField()),
                ('quest91Pos', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='session',
            old_name='chessScore',
            new_name='fisikScore',
        ),
        migrations.RenameField(
            model_name='session',
            old_name='footballScore',
            new_name='kognitifScore',
        ),
        migrations.RenameField(
            model_name='session',
            old_name='geographyScore',
            new_name='sosioScore',
        ),
        migrations.RemoveField(
            model_name='session',
            name='mathScore',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest10Ans',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest10Pos',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest10Scr',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest11Ans',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest11Pos',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest11Scr',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest12Ans',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest12Pos',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest12Scr',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest13Ans',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest13Pos',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest13Scr',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest14Ans',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest14Pos',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest14Scr',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest15Ans',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest15Pos',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest15Scr',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest16Ans',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest16Pos',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest16Scr',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest1Ans',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest1Pos',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest1Scr',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest2Ans',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest2Pos',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest2Scr',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest3Ans',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest3Pos',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest3Scr',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest4Ans',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest4Pos',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest4Scr',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest5Ans',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest5Pos',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest5Scr',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest6Ans',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest6Pos',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest6Scr',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest7Ans',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest7Pos',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest7Scr',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest8Ans',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest8Pos',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest8Scr',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest9Ans',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest9Pos',
        ),
        migrations.RemoveField(
            model_name='session',
            name='quest9Scr',
        ),
        migrations.AddField(
            model_name='session',
            name='mark',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='quizTest.sessionmark'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='order',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='quizTest.sessionorder'),
            preserve_default=False,
        ),
    ]
