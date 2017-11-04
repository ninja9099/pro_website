# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

image_path = 'static/blog/article_images'

article_states = [('published', 'Published'), ('draft', 'Draft'), ('approval', 'Approval'), ('archived', "Archived")]
class Article(TimeStampedModel):

    article_title = models.CharField(max_length=255, db_index=True,help_text="please provide title of your article", unique=True)
    article_image = models.ImageField(upload_to=image_path, height_field=None, width_field=None, blank=True, default="static/blog/article_images/default.png")
    article_category = models.ForeignKey('Category', on_delete=models.CASCADE)
    article_subcategory = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    article_followed = models.IntegerField(default=0)
    article_ratings = models.FloatField(default=0.0, blank=True)
    article_views = models.IntegerField(default=0)
    article_description = models.CharField(max_length=100, default=" ")
    article_content = models.CharField(max_length=5000)
    article_author = models.ForeignKey(User, blank=True)
    article_state = models.CharField(choices=article_states, default='draft', max_length=20)
    article_tags = models.TextField(blank=True, help_text="keaywords for indexing your article in search engins")
    article_flike_url = models.URLField('Like plugin url', blank=True)
    article_tags = models.ManyToManyField('ArticleTags')
    slug = models.SlugField(max_length=250)
    
    class Meta:
        ordering = ('-article_views', 'created',)

    @property
    def get_article_image(self):
        """
        return default imgae if image for article is not found  on server

        """
        try:
            return self.article_image.url
        except:
            return '/media/static/blog/article_images/default.png'


    def get_author_profile(self):
        return self.article_author.userprofile
    
    def get_absolute_url(self):
        return u'/article-edit/%d' % self.id 
        
    def __str__(self):
        return self.article_title 

    def count_likes(self):
        return len(self.articlelikes_set.all())



class Category(models.Model):
    category_name = models.CharField('Category',max_length=255, unique=True)

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    catagory_id = models.ForeignKey('Category', on_delete=models.CASCADE)
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

class ArticleTags(models.Model):
    tag_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag_name