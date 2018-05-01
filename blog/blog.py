# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import markdown
from django.db import models
from django.db.models import Count
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from autoslug import AutoSlugField


ARTICLE_IMAGE_PATH = settings.IMAGE_PATH + 'article_images'


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
    article_category = models.ForeignKey('Category', on_delete=models.CASCADE)
    article_subcategory = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    article_content = models.TextField('Article Content')
    article_author = models.ForeignKey(User,  related_name='article_written', on_delete=models.CASCADE)
    article_state = models.CharField(choices=ARTICLE_STATES_CHOICES, default='draft', max_length=20)
    slug = AutoSlugField(unique=True,populate_from='article_title')
    tags = TaggableManager()

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ('created',)   

    def __str__(self):
        return self.article_title

    def publish(self):
        self.article_state = 'published'
        return True;

    @property
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

    @staticmethod
    def get_counted_tags():
        tag_dict = {}
        query = Article.objects.filter(article_state='published').annotate(tagged=Count(
            'tags')).filter(tags__gt=0)
        for obj in query:
            for tag in obj.tags.names():
                if tag not in tag_dict:
                    tag_dict[tag] = 1

                else:  # pragma: no cover
                    tag_dict[tag] += 1
        return tag_dict.items()

    def get_summary(self):
        if len(self.article_content) > 255:
            return '{0}...'.format(self.article_content[:255])
        else:
            return self.article_content

    def get_summary_as_markdown(self):
        return markdown.markdown(self.get_summary(), safe_mode='escape')

    def get_author_profile(self):
        return self.article_author.userprofile

    def get_absolute_url(self):
        return u'/article-edit/%d' % self.id

    def count_likes(self):
        return self.articlelikes_set.all().count()


class Category(models.Model):
    category_name = models.CharField('Category', max_length=255, unique=True)
    category_image = models.ImageField(upload_to=ARTICLE_IMAGE_PATH, blank=True, default="default.png")

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    catagory_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class ArticleLikes(TimeStampedModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)

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
