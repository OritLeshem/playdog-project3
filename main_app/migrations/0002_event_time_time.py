# Generated by Django 3.1.7 on 2021-05-26 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='time_time',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]