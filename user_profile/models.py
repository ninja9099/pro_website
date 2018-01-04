# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from blog.blog import Article

PROFILE_PIC_PATH = settings.IMAGE_PATH + 'profile_images/'
cover_photo = 'static/src/images/user_profile/cover/'

user_type_choices = [(1, 'Admin'), (2, 'Moderator'), (3, 'Normal')]
default_image = settings.DEFAULT_USER_IMAGE


class UserProfile(models.Model):
    """
    Stores the additional information about the user
    which will be useful in running web blog
    """
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('notspecified', "Don't Specify")]

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    profile_picture = models.ImageField(upload_to=PROFILE_PIC_PATH, default=default_image,blank=True)
    birth_date = models.DateField('Birth Date', default='1900-01-01', blank=True, null=True)
    user_type = models.PositiveSmallIntegerField(choices=user_type_choices, null=False, help_text="Admin(1)/Moderator(2)/Normal(3)")
    gender = models.CharField(choices=GENDER_CHOICES, blank=True, default='notspecified', max_length=15)
    article_reads = models.ManyToManyField(Article, related_name="user_reads", blank=True) # fix the issue of not getting number
    about_me = models.TextField(blank=True, max_length=1000)
    short_intro = models.CharField(blank=True, max_length=100)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return "profile for %s" % self.user.username

    def get_articles_written(self):
        return self.user.article_set.all()

    @property
    def get_profile_image(self):
        """
        get profile image for the user and if not found returns  the 
        default images
        """
        try:
            return self.profile_picture.url
        except AttributeError:
            return settings.DEFAULT_USER_IMAGE

    @property
    def get_display_name(self):
        return self.user.first_name + self.user.last_name or self.user.username