
from blog import Article, ArticleRating, ArticleFollowings
from tastypie import fields
from django.contrib.auth.models import User
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization, DjangoAuthorization
from django.conf.urls import include, url

class UserResource(ModelResource):
    
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
    followings = fields.ToManyField(
        'blog.api.ArticleFollowingResource', 'followings', related_name='followings', full=True, null=True, blank=True)
    ratings = fields.ToManyField(
        'blog.api.ArticleRatingResource', 'rating', related_name='rating', full=True, null=True, blank=True)
    tags = fields.CharField(attribute='get_counted_tags', readonly=True)
    article_image = fields.CharField(attribute='get_article_image', readonly=True, null=True, blank=True)

    class Meta:
        queryset = Article.objects.all()
        resource_name = 'article'
        filtering = {
            'slug': ALL,
            'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }


class ArticleFollowingResource(ModelResource):
    article = fields.ToOneField(ArticleResource, 'article')
    user = fields.ToOneField(UserResource, 'user')
    
    class Meta:
        queryset = ArticleFollowings.objects.all()
        resource_name = 'following'
        fields = ["__all__"]

class ArticleRatingResource(ModelResource):
    rating_article = fields.ToOneField(ArticleResource, 'article')
    rating_user = fields.ToOneField(UserResource, 'user')
    class Meta:
        resource_name = 'rating'
        queryset = ArticleRating.objects.all()
        fields = [
            "__all__"
        ]
