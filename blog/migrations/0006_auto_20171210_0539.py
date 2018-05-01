# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_category_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_content',
            field=models.CharField(max_length=400000),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, upload_to='media/images/article_images'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, default='default.png', upload_to='media/images/article_images'),
        ),
    ]