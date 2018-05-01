from django.conf import settings
from django.conf.urls import url, include
from api import ArticleResource

article_resource = ArticleResource()

urlpatterns = [
    url(r'^', include(article_resource.urls)),
]