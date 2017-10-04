# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template import RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views import View
from .forms import ArticleFrom
from blog import Article
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import SimpleUploadedFile
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from collections import OrderedDict
from tracking_analyzer.models import Tracker
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.cache import cache_page

class ArticleUpdate(UpdateView):
    model = Article
    fields = ['article_title',
            'article_tags',
            'article_image',
            'article_category',
            'article_subcategory',
            'article_content',
            ]   
    template_name_suffix = '_update_form'


class ArticleListView(ListView):
    model= Article
    fields = ['article_title',
            'article_image',
            'article_category',
            'article_subcategory',
            'article_content',
            ]
    
    template_name_suffix = '_list_view'

@login_required
def article_edit(request, **kwargs):
    if request.method == 'GET':
        article_form = ArticleFrom()
        return render(request, 'blog/article_template.html', {"form":article_form})

    if request.method =='POST':
        form = ArticleFrom(request.POST, request.FILES)
        if form.is_valid() and form.is_multipart():
            article_instance = form.save(commit=False)
            article_instance.article_author= request.user
            article_instance.save()

        return render(request, 'blog/article_template.html', {"form":form} )


@cache_page(60 * 15)
def BlogIndex(request, **kwargs):
    '''
    view for Homepage of blog
    '''
    if request.method == "GET":
        query_set = Article.objects.all()
        paginator = Paginator(query_set[1:], 15)
        page = request.GET.get('page')

        try:
            article_page = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            article_page = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            article_page = paginator.page(paginator.num_pages)
        context = {}
        most_popular = query_set.order_by('-article_views')[0:4] 
        articles = query_set.order_by('-created')
        months= {1:'Jan', 2:'Fab',3:'Mar', 4:'Apr', 5:'May', 6:'Jun',7:'Jul',8:'Aug', 9:'Sep', 10:'Oct',11:'Nov', 12:'Dec'}
        context.update({'months': months, 'popular': most_popular, 'articles':articles, 'user':request.user, 'request':request})
        return render( request, 'blog/gallery.html',{'context':context, 'paginator':paginator, 'article_page':article_page})


def ArticleView(request, pk):
    '''View for displaying the article on the page includes analytics '''

    months= {1:'Jan', 2:'Fab',3:'Mar', 4:'Apr', 5:'May', 6:'Jun',7:'Jul',8:'Aug', 9:'Sep', 10:'Oct',11:'Nov', 12:'Dec'}
    article = get_object_or_404(Article, pk=pk, article_state='published')
    Tracker.objects.create_from_request(request, article)
    return render_to_response('blog/article.html',{"months": months, "article": article, "article_analytics": article_analytics(request)})

def article_analytics(request):
    query_set = Article.objects.order_by('-created')
    newest = query_set[0].created.year
    oldest = query_set.reverse()[0].created.year
    article_by_year = dict()
    for year in range(oldest, newest+1):
        try:
            temp = query_set.filter(created__year=year)
            article_by_year.update({year:{}})
            for month in range(1,13):
                if temp.filter(created__month=month):
                    article_by_year[year].update({month:temp.filter(created__month=month)})
        except:
            pass
    return article_by_year
