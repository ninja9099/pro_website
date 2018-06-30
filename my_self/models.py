# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from blog.blog import Article
from user_profile.models import User
# Create your models here.

default_image = "/default.png"
class MySelf(models.Model):
    user = models.OneToOneField(User,  related_name='related_user', on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to="", default=default_image, blank=True)
    authored = models.ManyToManyField(Article, blank=True)
    why_hire = models.CharField(max_length=30, blank=True)

class MyWork(models.Model):
    project_image = models.ImageField(upload_to="", default=default_image, blank=True)
    project_url = models.URLField()
    project_description = models.CharField(max_length=500)
    

class CarouselImages(models.Model):
    carousel_image_url = models.ImageField(upload_to="", default=default_image, blank=True)
    is_active = models.BooleanField(default=True)
    
class Services(models.Model):
    carousel_image_url = models.ImageField(upload_to="", default=default_image, blank=True)
    service_description = models.CharField(max_length=500)

class Team(models.Model):
    dev_name = models.CharField(max_length=255)
    dev_image = models.ImageField(upload_to="", default=default_image, blank=True)
    dev_exp = models.CharField(max_length=255, blank=True)


class CompanyInfo(models.Model):
    pass