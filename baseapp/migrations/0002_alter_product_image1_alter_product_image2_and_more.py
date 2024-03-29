# Generated by Django 4.0.1 on 2022-03-13 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.CharField(help_text='Write a brief description of the product here.', max_length=300),
        ),
    ]
