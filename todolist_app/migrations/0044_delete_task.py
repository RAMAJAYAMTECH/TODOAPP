# Generated by Django 4.0 on 2022-01-18 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0043_task'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]