# Generated by Django 3.0.5 on 2020-08-05 15:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_delete_progress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='leng',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='leng',
        ),
        migrations.AddField(
            model_name='quiz',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 5, 15, 23, 57, 342657, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 5, 15, 24, 18, 454676, tzinfo=utc)),
            preserve_default=False,
        ),
    ]