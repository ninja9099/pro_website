from blog import Article
from tastypie import fields
from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization, DjangoAuthorization


class UserResource(ModelResource):
   
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        allowed_methods = ['get']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = DjangoAuthorization()

        
class ArticleResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    class Meta:
        queryset = Article.objects.all()
        resource_name = 'article'

