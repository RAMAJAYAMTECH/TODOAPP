# Generated by Django 4.0 on 2022-01-27 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0058_rename_file_work_file2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='file2',
            new_name='file',
        ),
    ]
