# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-10 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180810_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletags',
            name='fake_field',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]