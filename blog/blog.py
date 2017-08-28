# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
import collections
import copy
import datetime
import decimal
import itertools
from base64 import b64decode, b64encode
from functools import total_ordering
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User

image_path = 'static/blog/article_images'
# Create your models here.
article_states = [('published', 'Published'), ('draft', 'Draft'), ('approval', 'Approval'), ('archived', "Archived")]
class Article(TimeStampedModel):

	article_title = models.CharField(max_length=255, db_index=True,help_text="please provide title of your article", unique=True)
	article_image = models.ImageField(upload_to=image_path, height_field=None, width_field=None)
	article_category = models.ForeignKey('Category', on_delete=models.CASCADE)
	article_subcategory = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
	article_followed = models.IntegerField(default=0)
	article_ratings = models.FloatField(default=0.0, blank=True)
	article_views = models.IntegerField(default=0)
	article_content = models.TextField()
	article_author = models.ForeignKey(User, blank=True)
	article_state= models.CharField(choices=article_states, default='draft', max_length=20)



	def __str__(self):
		return self.article_title

class Category(models.Model):
	category_name = models.CharField('Category',max_length=255, unique=True)

	def __str__(self):
		return self.category_name

class SubCategory(models.Model):
	catagory_id = models.OneToOneField('Category', on_delete=models.CASCADE)
	category_name = models.CharField(max_length=255)

	def __str__(self):
		return self.category_name

class ArticleLikes(TimeStampedModel):
	user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	article_id = models.ForeignKey(Article, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Article like'
		verbose_name_plural = 'Article Likes'
		unique_together = (("article_id", "user_id"),)