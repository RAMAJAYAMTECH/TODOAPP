# Generated by Django 4.0 on 2022-01-06 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0041_gst_master_delete_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gst_master',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]