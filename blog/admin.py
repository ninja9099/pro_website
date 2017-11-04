# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from . blog import Article, Category,SubCategory, ArticleLikes

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['category_name',]

class SubCategoryAdmin(admin.ModelAdmin):
	list_display= ['category_name', 'catagory_id']


class ArticleAdmin(admin.ModelAdmin):
	list_display = ['article_title',
		'article_author',
		'article_image',
		'article_category',
		'article_subcategory',
		'article_followed',
		'article_ratings',
		'article_views',
		'created',
		'modified',
	]
	list_filter = ['article_author', 'article_subcategory']
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)


class ArticleLikesAdmin(admin.ModelAdmin):
	list_display= ['user_id', 'article_id']

admin.site.register(ArticleLikes, ArticleLikesAdmin)