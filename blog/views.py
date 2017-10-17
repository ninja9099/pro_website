# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template import RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views import View
from .forms import ArticleFrom
from blog import Article, ArticleLikes, ArticleTags
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.core.files.uploadedfile import SimpleUploadedFile
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from collections import OrderedDict
from tracking_analyzer.models import Tracker
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.cache import cache_page

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
@permission_required('blog.change_article', raise_exception=True)
def article_edit(request, **kwargs):
    
    if request.method =='GET':
        if kwargs.get('pk', 'false'): 
            article = get_object_or_404(Article, pk=kwargs.get('pk'))
            if request.user == article.article_author:
                form  = ArticleFrom(instance=article)
                return render(request, 'blog/article_template.html', {"form":form} )
            else:
                return HttpResponse('<h1>Error 403 Not Allowed</h1>')
        else:
            article_form = ArticleFrom()
            return render(request, 'blog/article_template.html', {"form":article_form})

    if request.method =='POST':
        form = ArticleFrom(request.POST, request.FILES)
        if form.is_valid() and form.is_multipart():
            article_instance = form.save(commit=False)
            article_instance.article_author= request.user
            article_instance.save()

        return render(request, 'blog/article_template.html', {"form":form} )


def user_liked(user_id, article_id):
    try:
        if len(ArticleLikes.objects.filter(article_id=article_id, user_id=user_id)):
            print user_id,  article_id
            return True
    except:
        return False

def BlogIndex(request, **kwargs):
    '''
    view for Homepage of blog
    '''
    # prepare for launching the jason data
    articles_json = []
    if request.method == "GET":
        
        query_set = Article.objects.all().order_by('-article_views',  '-created')
        paginator = Paginator(query_set, 15)
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
        for item  in article_page.object_list:
            articles_json.append({
                'article':item,
                "likes":item.count_likes(),
                "user_liked":user_liked(request.user.id, item.id)
                })
        return render( request, 'blog/gallery.html', { 'article_page':article_page, 'articles_json': articles_json})


def ArticleView(request, pk):
    '''View for displaying the article on the page includes analytics '''
    
    months= {1:'Jan', 2:'Fab',3:'Mar', 4:'Apr', 5:'May', 6:'Jun',7:'Jul',8:'Aug', 9:'Sep', 10:'Oct',11:'Nov', 12:'Dec'}
    article = get_object_or_404(Article, pk=pk, article_state='published')
    Tracker.objects.create_from_request(request, article)
    return render_to_response('blog/article.html',{'tags':ArticleTags.objects.all(), "months": months, "article": article, "article_analytics": article_analytics(request)})

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
