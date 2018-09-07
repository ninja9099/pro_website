from django.conf.urls import url, include
from blog import views as api_views
from rest_framework.authtoken import views
from .views import CustomObtainAuthToken


urlpatterns = [
    url(r'^api-token/', CustomObtainAuthToken.as_view()),
    url(r'^articles/$', api_views.article_list),
    url(r'^articles/(?P<pk>[0-9]+)/$', api_views.article_detail),
    url(r'^tags/$', api_views.tag_list),
    url(r'^tags/(?P<pk>[0-9]+)/$', api_views.tag_detail),
    url(r'^category/$', api_views.category_list),
    url(r'^category/(?P<pk>[0-9]+)/$', api_views.category_detail),
    url(r'^subcategory/$', api_views.subcategory_list),
    url(r'^subcategory/(?P<pk>[0-9]+)/$', api_views.subcategory_detail),
]
