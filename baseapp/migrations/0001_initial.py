# Generated by Django 4.0.1 on 2022-02-15 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Write the title within 200 characters.', max_length=256)),
                ('description', models.TextField(help_text='Write a desctiprion of this blog in a few sentences')),
                ('body', models.TextField(help_text='Your main content goes here.')),
                ('views', models.IntegerField(default=0, help_text='This statistic is for your reference, do not change it.')),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('privacy', models.CharField(choices=[('PRIVATE', 'Private'), ('PUBLIC', 'Public')], default='PRIVATE', help_text='Public posts will appear to everyone and private posts only to you. Change this to private instead of deleting a post.', max_length=10)),
                ('slug', models.SlugField(blank=True, help_text='Leave this parameter empty, it will get generated automatically.')),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('discount_percentage', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=100)),
                ('val', models.FloatField(blank=True, help_text='Do NOT change this field. It gets updated automatically.')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('one_line_description', models.CharField(blank=True, default='', help_text='Describe the course in one but unforgettable line. Max 300 characters', max_length=300)),
                ('description', models.TextField(unique=True)),
                ('image_url', models.CharField(default='', help_text='Enter Image URL within 200 characters.', max_length=200)),
                ('high_price', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, help_text='Leave this parameter empty, it will get generated automatically.', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, unique=True)),
                ('high_price', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('image1', models.TextField(default='', max_length=200)),
                ('image2', models.TextField(default='', max_length=200)),
                ('image3', models.TextField(default='', max_length=200)),
                ('slug', models.SlugField(blank=True, help_text='Leave this parameter empty, it will get generated automatically.')),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('landmark', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Details',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.TextField(help_text="Customer's Orders")),
                ('total_cost', models.IntegerField(default=0)),
                ('code_applied', models.CharField(default='', max_length=20)),
                ('discounted_cost', models.IntegerField(default=0)),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('address1', models.CharField(default='', max_length=100)),
                ('address2', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('pincode', models.CharField(default='', max_length=50)),
                ('landmark', models.CharField(default='', max_length=50)),
                ('ordered_at', models.DateTimeField(auto_now_add=True, help_text='Do NOT change this date and time field.')),
                ('last_changed_at', models.DateTimeField(auto_now=True, help_text='Do NOT change this date and time field.')),
                ('status', models.CharField(choices=[('OPS', 'Order Placed Successfully'), ('S', 'Shipped'), ('OFD', 'Out For Delivery'), ('D', 'Delivered')], default='Order Placed Successfully', help_text='Change this only when you are sure. This sends an email to the user regarding the update.', max_length=5)),
                ('user', models.ForeignKey(help_text='User who placed this order.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('one_line_description', models.CharField(blank=True, default='', help_text='Describe the lecture in one but unforgettable line. Max 300 characters', max_length=300)),
                ('description', models.TextField(unique=True)),
                ('youtube_url', models.CharField(max_length=100, unique=True)),
                ('course_index', models.IntegerField(unique=True)),
                ('slug', models.SlugField(blank=True, help_text='Leave this parameter empty, it will get generated automatically.', unique=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseapp.course')),
            ],
        ),
    ]
