# Generated by Django 3.0.6 on 2020-06-06 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0007_auto_20200605_1400'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ['-created']},
        ),
    ]
