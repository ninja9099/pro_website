
from blog import Article
from tastypie import fields
from django.contrib.auth.models import User
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization, DjangoAuthorization
from django.conf.urls import include, url

class UserResource(ModelResource):
    
    fullname = fields.CharField(attribute="get_full_name", readonly=True)
    articles_authored = fields.ToManyField(
        'blog.api.ArticleResource', 'article_written', related_name='article_written')
    
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        allowed_methods = ['get']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = DjangoAuthorization()


class ArticleResource(ModelResource):
    
    author = fields.ToOneField(UserResource, 'article_author', full=True)
    
    class Meta:
        queryset = Article.objects.all()
        resource_name = 'article'
        filtering = {
            'slug': ALL,
            'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
