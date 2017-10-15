# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-15 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0017_userprofile_short_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cover_photo',
            field=models.ImageField(blank=True, default='static/src/images/user_profile/img/avatar.png', upload_to='static/src/images/user_profile/cover/'),
        ),
    ]