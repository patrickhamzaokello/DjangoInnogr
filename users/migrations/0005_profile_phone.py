# Generated by Django 3.0.8 on 2020-07-12 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='Add Phone Number', max_length=20),
        ),
    ]
