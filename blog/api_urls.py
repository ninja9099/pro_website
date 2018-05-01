from django.conf import settings
from django.conf.urls import url, include
from api import ArticleResource, UserResource
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(ArticleResource())

urlpatterns = [
    url(r'^', include(v1_api.urls)),
]