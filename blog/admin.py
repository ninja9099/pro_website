# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from .blog import (Article, 
    Category,
    SubCategory, 
    ArticleLikes,
    ArticleRating,
    ArticleFollowings)
from django_summernote.admin import SummernoteModelAdmin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', ]


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'catagory_id']


class ArticleAdmin(SummernoteModelAdmin):
    list_display = ['article_title',
                    'slug',
                    'article_author',
                    'article_image',
                    'article_category',
                    'article_subcategory',
                    'created',
                    'modified',
                    ]
    list_filter = ['article_author', 'article_subcategory']
    summer_note_fields = ('article_content',)


class ArticleLikesAdmin(admin.ModelAdmin):
    list_display = [
        'user_id', 
        'article_id'
        ]
    list_filter = ['user_id']


class ArticleRatingAdmin(admin.ModelAdmin):
    
    list_display = [
        'user',
        'article',
        'article_ratings',
        'feedbacks'
        ]
    list_filter = ['article_ratings', 'user']



class ArticleFollowingsAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'article',
        'is_followed',
    ]
    list_filter = ['user']
admin.site.register(ArticleLikes, ArticleLikesAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(ArticleRating, ArticleRatingAdmin)
admin.site.register(ArticleFollowings, ArticleFollowingsAdmin)
