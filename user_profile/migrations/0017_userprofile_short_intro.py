# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-15 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0016_auto_20171011_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='short_intro',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
