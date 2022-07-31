# Generated by Django 3.0.9 on 2021-11-23 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0024_auto_20211123_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='edit_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updatedate', models.DateField(blank=True, null=True)),
                ('time_from', models.TimeField(blank=True, null=True)),
                ('time_to', models.TimeField(blank=True, null=True)),
                ('messagelogs', models.TextField(blank=True, null=True)),
                ('file', models.FileField(null=True, upload_to='')),
                ('old_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todolist_app.Tasklist')),
            ],
        ),
        migrations.CreateModel(
            name='doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='')),
                ('d_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todolist_app.Tasklist')),
            ],
        ),
    ]