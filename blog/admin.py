# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from .models import (Article, 
    Category,
    SubCategory, 
    ArticleLikes,
    ArticleRating,
    ArticleFollowings,
    ArticleTags,)

from django import forms


class ArticleTagsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', ]


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'catagory_id']




class ArticleAdmin(admin.ModelAdmin):
    list_display = ['article_title',
                    'slug',
                    'article_image',
                    'article_category',
                    'article_subcategory',
                    'created',
                    'modified',
                    ]
    list_filter = ['article_subcategory']


class ArticleLikesAdmin(admin.ModelAdmin):
    list_display = [
        'user_id', 
        'article_id'
        ]
    list_filter = ['user_id']


class ArticleRatingForm(forms.ModelForm):
    class Meta:
        model = ArticleRating
        fields = ("__all__")
    
    def clean(self):
        article_rating = self.cleaned_data.get('article_ratings')
       
        if article_rating > 5 or article_rating < 0:
            raise forms.ValidationError("Rating is 0 To 5 only ")
        return self.cleaned_data


class ArticleRatingAdmin(admin.ModelAdmin):
    form = ArticleRatingForm
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
admin.site.register(ArticleTags, ArticleTagsAdmin)
