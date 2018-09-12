# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import markdown
from django.db import models
from django.db.models import Count
from model_utils.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from autoslug import AutoSlugField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.functional import cached_property
import uuid
from django.contrib.auth import get_user_model

import boto3



def upload_to_s3(image, key):
    s3 = boto3.client("s3", region_name="", aws_access_key_id="", aws_secret_access_key="")

    res = s3.put_object(Body=image, Bucket='', Key=key)
    try:
        url = settings.S3_BASE_URL + str(key)
    except :
        raise Exception("please define the s3 bcket path for image upload to s3 or remove that field from modal")
    return url




User = get_user_model()
ARTICLE_IMAGE_PATH = settings.IMAGE_PATH + 'article_images'

class ArticleTags(models.Model):
    name = models.CharField(max_length=100,blank=True)
    slug = AutoSlugField(unique=True, populate_from='name')
    def __str__(self):
        return "%s:%s" %(self.id, self.slug)

class Article(TimeStampedModel):

    ARTICLE_STATES_CHOICES = [
        ('published', 'Published'), 
        ('draft', 'Draft'), 
        ('approval', 'Approval'), 
        ('archived', "Archived")
        ]
    article_title = models.CharField(max_length=255, db_index=True, help_text="please provide title of your article",
                                     unique=True)
    article_image = models.ImageField(upload_to=ARTICLE_IMAGE_PATH, height_field=None, width_field=None, blank=True)
    article_category = models.ForeignKey('Category', related_name="cat_set", on_delete=models.CASCADE, null=True)
    article_subcategory = models.ForeignKey('SubCategory',related_name="sucat_set", on_delete=models.CASCADE, null=True)
    article_content = models.TextField('Article Content', null=True)
    article_author = models.ForeignKey(User,  related_name='article_written', on_delete=models.CASCADE)
    article_state = models.CharField(choices=ARTICLE_STATES_CHOICES, default='draft', max_length=20)
    article_slug = AutoSlugField(unique=True,populate_from='article_title')
    article_tags = models.ManyToManyField(ArticleTags, related_name='tagged_articles', blank=True, verbose_name='tags')
    # _s3_image_path = models.URLField(max_length=1000)

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ('created',)


    def __str__(self):
        return "%s:%s" %(self.id, self.article_slug)

    def publish(self):
        self.article_state = 'published'
        return True;

    def get_article_image(self):
        """
        return default image if image for article is not found  on server

        """
        try:
            return self.article_image.url
        except ValueError:
            return settings.DEFAULT_ARTICLE_IMAGE

    def get_content_as_markdown(self):
        return markdown.markdown(self.article_content, safe_mode='escape')

    @classmethod
    def get_published(cls):
        articles = cls.objects.filter(article_state='published')
        return articles

    @cached_property
    def get_all_comments(self):
        return list([item for item in self.comment_comments.all()])
    
    @staticmethod
    def get_counted_tags():
        tag_dict = {}
        query = Article.objects.filter(article_state='published').annotate(tagged=Count(
            'tagged_articles')).filter(tags__gt=0)
        for obj in query:
            for tag in obj.tags.names():
                if tag not in tag_dict:
                    tag_dict[tag] = 1

                else:  # pragma: no cover
                    tag_dict[tag] += 1
        return tag_dict.items()

    def get_summary(self):
        return '{0}...'.format(self.article_content)
     

    def get_summary_as_markdown(self):
        return markdown.markdown(self.get_summary(), safe_mode='escape')

    def save(self, *args, **kwargs):
        # url = upload_to_s3(self.article_image, self.article_image.name)
        # self._s3_image_path = url
        super(Article, self).save(*args, **kwargs)



class Category(models.Model):
    category_name = models.CharField('Category', max_length=255, unique=True)
    category_image = models.ImageField(upload_to=ARTICLE_IMAGE_PATH, blank=True, default="default.png")

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    catagory_id = models.ForeignKey('Category', related_name='sub_categories',)
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class ArticleLikes(TimeStampedModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Article like'
        verbose_name_plural = 'Article Likes'
        unique_together = (("article_id", "user_id"),)


class ArticleRating(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='rating', on_delete=models.CASCADE)
    article_ratings = models.FloatField(default=0.0, blank=True)
    feedbacks = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name = 'Article Rating'
        verbose_name_plural = 'Article Ratings'
        unique_together = (("user", "article"),)


class ArticleFollowings(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='followings', on_delete=models.CASCADE)
    is_followed = models.BooleanField(default=True)
    class Meta:
        unique_together = (("user", "article"),)
