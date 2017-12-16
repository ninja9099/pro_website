# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import forms
from blog import Article
from taggit.forms import TagWidget
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core import exceptions

class ArticleForm(forms.ModelForm):
    """ Form for the article writing and submission"""
    article_content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = Article
        fields = [
            'article_title',
            'article_image',
            'article_category',
            'article_subcategory',
            'article_content',
            'tags'
        ]
        widget={
        'tags': TagWidget()
        }
