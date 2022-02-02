# Generated by Django 4.0.1 on 2022-02-02 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='course_index',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='description',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='slug',
            field=models.SlugField(blank=True, help_text='Leave this parameter empty, it will get generated automatically.', unique=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='youtube_url',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
