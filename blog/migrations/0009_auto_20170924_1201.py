# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-24 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170829_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='catagory_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category'),
        ),
    ]
