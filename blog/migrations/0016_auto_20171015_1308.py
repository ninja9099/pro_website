# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-15 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20171013_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, upload_to='static/blog/article_images'),
        ),
    ]