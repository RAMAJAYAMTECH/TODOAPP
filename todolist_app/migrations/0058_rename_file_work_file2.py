# Generated by Django 4.0 on 2022-01-27 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0057_work'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='file',
            new_name='file2',
        ),
    ]