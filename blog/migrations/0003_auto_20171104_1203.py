# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171104_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=250),
        ),
    ]
