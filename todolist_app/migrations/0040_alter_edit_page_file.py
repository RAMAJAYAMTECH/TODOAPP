# Generated by Django 3.2.10 on 2021-12-25 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0039_alter_edit_page_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edit_page',
            name='file',
            field=models.FileField(default=True, upload_to=''),
        ),
    ]