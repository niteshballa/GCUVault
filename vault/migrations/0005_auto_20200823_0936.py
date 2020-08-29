# Generated by Django 3.0.5 on 2020-08-23 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0004_auto_20200822_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='action',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='adv',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='comedy',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='drama',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='fantasy',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='horror',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='romance',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='scifi',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='thriller',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
