# Generated by Django 3.2.2 on 2021-05-22 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210521_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='events',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='user',
        ),
        migrations.AddField(
            model_name='dog',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='dog',
            name='image',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dog',
            name='size',
            field=models.CharField(choices=[('T', 'TINY'), ('S', 'SMALL'), ('M', 'MEDIUM'), ('L', 'LARGE'), ('X', 'EXTRA LARGE')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(to='main_app.Dog'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.FloatField(),
        ),
    ]