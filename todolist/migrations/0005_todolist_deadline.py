# Generated by Django 3.0.6 on 2020-06-01 13:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_auto_20200601_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='deadline',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]