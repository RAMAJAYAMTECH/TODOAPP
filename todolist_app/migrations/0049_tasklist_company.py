# Generated by Django 4.0 on 2022-01-19 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0048_remove_tasklist_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
