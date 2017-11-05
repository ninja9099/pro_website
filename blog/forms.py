# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import forms
from blog import Article
from taggit.forms import TagWidget
class ArticleForm(forms.ModelForm):
    """ Form for the article writting and submission"""
    article_content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        max_length=4000)
    tags = forms.CharField(
        widget=TagWidget(attrs={'class': 'form-control'}), max_length=255)
    

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
