# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from blog.blog import Article

profile_folder = 'static/src/images/user_profile/img/'
user_type_choices = [(1, 'Admin'), (2, 'Moderator'), (3, 'Normal')]
gender_choices = [('m', 'Male'), ('f', 'Female'),('n', 'Dont Specify')]
class UserProfile(models.Model):

    """Stores the additional information about the user 
    which will be usefull in running web blog"""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    profile_picture = models.ImageField(upload_to=profile_folder, height_field=None, width_field=None, max_length=100)
    birth_date = models.DateField('Birth Date', default='1900-01-01', blank=True, null=True)
    address = models.TextField(max_length=300, blank=True)
    mobile = models.CharField(max_length=10, unique=True, null=False, blank=False)
    user_type = models.PositiveSmallIntegerField(choices=user_type_choices, null=False, blank=True, help_text="Admin(1)/Moderator(2)/Normal(3)")
    gender = models.CharField(choices=gender_choices, blank=True, max_length=1)
    article_reads = models.ManyToManyField(Article, related_name="user_reads", blank=True) # fix the issue of not getting number
    about_me = models.TextField(blank=True, max_length=1000)
    is_active = models.BooleanField(default=True)
    


    def __unicode__(self):
        return "%s  %s --> %s" % (self.user.first_name, self.user.last_name, self.user.username)

    def get_articles_written(self):
        import pdb
        pdb.set_trace()
        user = self.user
        articles_written = user.article_set.all()
        return articles_written

