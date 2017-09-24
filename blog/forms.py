# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import forms
from blog import Article
class ArticleFrom(forms.ModelForm):
    """ Form for the article writting and submission"""
    class Meta:
        model = Article
        fields = ['article_title',
            'article_image',
            'article_category',
            'article_subcategory',
            'article_content',
        ]