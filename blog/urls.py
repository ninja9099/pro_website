# -*- coding: utf-8 -*-

"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from blog_api import api_views
from . import views
from rest_framework import routers
from blog_api import api


router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'groups', api_views.GroupViewSet)


urlpatterns=[
    url(r'^$',views.BlogIndex, name="blog_home" ),
    url(r'rest_api^', include(router.urls)),
    url(r'^article/(?P<pk>\d+)', views.ArticleView, name="article"),
    url(r'^article_submitt/$', views.create_article, name="article_submit"),
    url(r'^article_edit/(?P<pk>\d+)$', views.edit_article, name="article_edit"),
    url(r'^article_likes/(?P<pk>\d+)$', api.article_likes, name="article_likes"),
]