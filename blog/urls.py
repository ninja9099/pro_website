from django.conf.urls import url, include
from blog import views as api_views
from rest_framework.authtoken import views
from .views import CustomObtainAuthToken, EditoreUploadImage


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
    url(r'^likes/$', api_views.like_list),
    url(r'^likes/(?P<article_id>[0-9]+)/$', api_views.like_detail),
    url(r'^users/$', api_views.user_list),
    url(r'^users/(?P<user_id>[0-9]+)/$', api_views.user_detail),
    url(r'^editor/image/', EditoreUploadImage.as_view(), name="editor_image_upload")
]
