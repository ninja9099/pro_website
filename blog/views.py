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


