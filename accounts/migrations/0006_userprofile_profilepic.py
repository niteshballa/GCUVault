# Generated by Django 3.0.5 on 2020-08-04 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userprofile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profilepic',
            field=models.ImageField(default='NULL', upload_to='Profilepics'),
            preserve_default=False,
        ),
    ]
