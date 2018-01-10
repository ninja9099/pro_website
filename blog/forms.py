# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import forms
from blog import Article
from taggit.forms import TagWidget
from django_summernote.fields import SummernoteTextFormField


class ArticleForm(forms.ModelForm):
    """ Form for the article writing and submission"""

    article_content = SummernoteTextFormField()

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
        'tags': TagWidget(),
        }
