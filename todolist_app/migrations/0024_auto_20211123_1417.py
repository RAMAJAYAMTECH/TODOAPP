# Generated by Django 3.0.9 on 2021-11-23 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0023_doc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edit_page',
            name='old_id',
        ),
        migrations.DeleteModel(
            name='doc',
        ),
        migrations.DeleteModel(
            name='edit_page',
        ),
    ]
