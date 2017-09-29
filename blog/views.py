# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
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

class ArticleUpdate(UpdateView):
    model = Article
    fields = ['article_title',
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

@login_required
def BlogIndex(request, **kwargs):
    
    articles = Article.objects.all()
    if request.method == "GET":
        return render_to_response('pages/gallery.html',{"articles": articles, 'user':request.user})


def ArticleView(request, pk):
    months= {1:'Jan', 2:'Fab',3:'Mar', 4:'Apr', 5:'May', 6:'Jun',7:'Jul',8:'Aug', 9:'Sep', 10:'Oct',11:'Nov', 12:'Dec'}
    try:
        article = Article.objects.get(id=pk, article_state='published')
    except Exception as e:
        return render_to_response('misc/404.html',)
    return render_to_response('blog/article.html',{"months": months, "article": article, "article_analytics": article_analytics(request)})

def article_analytics(request):
    import pdb
    pdb.set_trace()
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
