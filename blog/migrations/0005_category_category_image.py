# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171105_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, default='static/blog/category/default.png', upload_to=b'static/blog/article_images'),
        ),
    ]