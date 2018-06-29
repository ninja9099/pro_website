# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-29 04:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0002_article_article_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel_image_url', models.ImageField(blank=True, default='/default.png', upload_to='')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MySelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('profile_picture', models.ImageField(blank=True, default='/default.png', upload_to='')),
                ('why_hire', models.CharField(blank=True, max_length=30)),
                ('authored', models.ManyToManyField(blank=True, to='blog.Article')),
            ],
        ),
        migrations.CreateModel(
            name='MyWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_image', models.ImageField(blank=True, default='/default.png', upload_to='')),
                ('project_url', models.URLField()),
                ('project_description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel_image_url', models.ImageField(blank=True, default='/default.png', upload_to='')),
                ('service_description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_name', models.CharField(max_length=255)),
                ('dev_image', models.ImageField(blank=True, default='/default.png', upload_to='')),
                ('dev_exp', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
