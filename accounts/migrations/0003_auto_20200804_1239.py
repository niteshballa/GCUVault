# Generated by Django 3.0.5 on 2020-08-04 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_auto_20200804_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(default='NULL', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='parquiztime',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='parwklyquiz',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='parwkndquiz',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='quiztime',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weekendquiz',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weeklyquiz',
            field=models.IntegerField(default=0),
        ),
    ]
