# Generated by Django 3.0.6 on 2020-06-05 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_auto_20200601_1544'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ['created']},
        ),
    ]