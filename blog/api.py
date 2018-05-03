
from blog import Article, ArticleRating, ArticleFollowings
from tastypie import fields
from django.contrib.auth.models import User
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization, DjangoAuthorization
from django.conf.urls import include, url


from tastypie.fields import ListField
from taggit.models import Tag, TaggedItem

class TaggedResource(ModelResource):
    tags = ListField()

    class Meta:
        queryset = Tag.objects.all()

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
    # followings = fields.ToManyField(
    #     'blog.api.ArticleFollowingResource', 'followings', related_name='followings', full=True, null=True, blank=True)
    ratings = fields.ToManyField(
        'blog.api.ArticleRatingResource', 'rating', related_name='rating', full=True, null=True, blank=True)
    article_tags = fields.ToManyField('blog.api.TaggedResource', 'tags',  full=True)
    article_image = fields.CharField(
        attribute='get_article_image', readonly=True, null=True, blank=True)
    follow_list = fields.ListField()
    total_rating = fields.FloatField()
    class Meta:
        queryset = Article.objects.all()
        resource_name = 'article'
        filtering = {
            'slug': ALL,
            'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }

    def dehydrate_follow_list(self, bundle):
        return list(set(bundle.obj.followings.filter(is_followed=True).values_list('user', flat=True)))

    def dehydrate_total_rating(self, bundle):
        toatal_rating = 0.0
        s = reduce(lambda x, y : x + y, [rating.article_ratings for rating in bundle.obj.rating.all()])
        return s/bundle.obj.rating.all().count()

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
