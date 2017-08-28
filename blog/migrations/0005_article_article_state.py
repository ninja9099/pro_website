# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-27 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170821_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_state',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft'), ('approval', 'Approval'), ('archived', 'Archived')], default='draft', max_length=20),
        ),
    ]
