# Generated by Django 3.0.4 on 2020-07-14 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('innogrApp', '0004_post_last_edited'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
