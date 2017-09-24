# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.views import View
from .forms import ArticleFrom
from blog import Article
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import SimpleUploadedFile

@login_required
def article_edit(request, **kwargs):

	if request.method == 'GET':
		article_form = ArticleFrom()
		return render(request, 'blog/article_template.html', {"form":article_form})

	if request.method =='POST':
		import pdb
		pdb.set_trace()
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
		return render_to_response('pages/gallery.html',{"articles": articles})