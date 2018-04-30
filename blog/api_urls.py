
from . import views
from blog_api import api
from django.conf.urls import url  # include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^article/$', api.article_list),
    url(r'^article/(?P<pk>[0-9]+)/$', api.article_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)