# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from blog.blog import Article, ArticleLikes
from django.template import RequestContext
from blog.blog import Category
from django.db.models import Count, F

def create_context(request):
    context = RequestContext(request)
    article_set = Article.get_published().order_by('-article_views', '-created').annotate(likes=Count('articlelikes'))
    categories = Category.objects.annotate(articles=Count('article')).order_by('-articles')
    context.push({
        'categories': categories,
        'popular_tags': Article.get_counted_tags(),
        'article_set': article_set,
    })
    return context
