# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-11 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0014_auto_20171011_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, height_field=200, upload_to='static/src/images/user_profile/img/', width_field=200),
        ),
    ]
