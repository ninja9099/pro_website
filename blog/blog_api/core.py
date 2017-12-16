# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from blog.blog import Article #ArticleLikes
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


def article_analytics(request, article_set):
    query_set = article_set.order_by('-created')
    newest = query_set[0].created.year
    oldest = query_set.reverse()[0].created.year
    article_by_year = dict()
    for year in range(oldest, newest+1):
        try:
            temp = query_set.filter(created__year=year)
            article_by_year.update({year:{}})
            for month in range(1,13):
                by_month = temp.filter(created__month=month)
                if by_month:
                    article_by_year[year].update({by_month[0].created:temp.filter(created__month=month)})
        except:
            pass
    return article_by_year

# for future use
def handle_uploaded_file(f, type=None):
    import pdb
    pdb.set_trace()
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)