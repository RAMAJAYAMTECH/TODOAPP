# Generated by Django 3.0.9 on 2021-10-23 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0003_auto_20211023_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edit_page',
            name='old_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todolist_app.Tasklist'),
        ),
    ]