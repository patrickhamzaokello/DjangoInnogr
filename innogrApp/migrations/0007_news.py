# Generated by Django 3.0.4 on 2020-07-19 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('innogrApp', '0006_auto_20200717_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('link', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=300)),
            ],
        ),
    ]
