# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-03 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_article_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_flike_url',
            field=models.URLField(blank=True, verbose_name='Like plugin url'),
        ),
    ]
