
from blog import Article, ArticleRating, ArticleFollowings, Category, SubCategory
from tastypie import fields

from tastypie.resources import ModelResource, Resource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization, DjangoAuthorization
from django.conf.urls import include, url
from user_profile.models import User

from tastypie.fields import ListField
from taggit.models import Tag, TaggedItem
from my_self.models import MySelf, MyWork,CarouselImages,Services,Team,CompanyInfo




class MySelfResource(ModelResource):
    class Meta:
        queryset = MySelf.objects.all()
        resource_name = 'myself'
        excludes = []
        allowed_methods = ['get']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = DjangoAuthorization()


class MyWorkfResource(ModelResource):
    class Meta:
        queryset = MyWork.objects.all()
        resource_name = 'mywork'
        excludes = []
        allowed_methods = ['get']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = DjangoAuthorization()


class ServicesResource(ModelResource):
    class Meta:
        queryset = Services.objects.all()
        resource_name = 'services'
        excludes = []
        allowed_methods = ['get']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = DjangoAuthorization()


class TeamResource(ModelResource):
    class Meta:
        queryset = Team.objects.all()
        resource_name = 'team'
        excludes = []
        allowed_methods = ['get']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = DjangoAuthorization()

class HomePageResources(ModelResource):
   
    mywork = fields.ToManyField('MyWorkfResource', 'mywork',null=True, blank=True)
    services = fields.ToManyField('ServicesResource', 'services',null=True, blank=True)
    # team = fields.ForeignKey('TeamResource', 'team',null=True, blank=True)
    carousel_images = fields.ListField(null=True, blank=True)

    class Meta:
        queryset = MySelf.objects.all()
        resource_name = 'homepageresource'
        allowed_methods = ['get']
        authorization = DjangoAuthorization()

    def dehydrate_carousel_images(self, bundle):
        return list(CarouselImages.objects.all().values_list('carousel_image_url', flat=True))


class TaggedResource(ModelResource):
    tags = ListField()

    class Meta:
        queryset = Tag.objects.all()

class UserResource(ModelResource):
    
    articles_authored = fields.ToManyField('blog.api.ArticleResource', 'article_written', related_name='article_written')
    comments = ListField(attribute='get_all_comments', readonly=True)
    full_name = fields.CharField(attribute="get_full_name", readonly=True)
    article_reads = ListField(attribute='get_article_reads', readonly=True)
    profile_picture = fields.CharField(attribute='get_profile_image', readonly=True)
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        allowed_methods = ['get']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = DjangoAuthorization()



class ArticleResource(ModelResource):
    
    author = fields.ForeignKey(UserResource, 'article_author', full=True)
    article_tags = fields.ToManyField('blog.api.TaggedResource', 'tags',  full=True)
    article_image = fields.CharField(
        attribute='get_article_image', readonly=True, null=True, blank=True)
    follow_list = fields.ListField(null=True, blank=True)
    total_rating = fields.FloatField()
    likes = ListField(attribute='get_likes', readonly=True)
    comments = ListField()
    total_reads = fields.IntegerField()

    class Meta:
        queryset = Article.objects.filter(article_state="published")
        resource_name = 'article'
        filtering = {
            'slug': ALL,
            'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }

    def dehydrate_follow_list(self, bundle):
        return list(set(bundle.obj.followings.filter(is_followed=True).values_list('user', flat=True)))

    def dehydrate_total_rating(self, bundle):
        toatal_rating = 0.0
        if bundle.obj.rating.exists():
            s = reduce(lambda x, y : x + y, [rating.article_ratings for rating in bundle.obj.rating.all()])
            toatal_rating = s/bundle.obj.rating.all().count()
        return toatal_rating

    def dehydrate_total_reads(self, bundle):
        total_reads = 0
        if bundle.obj.user_reads.exists():
            return bundle.obj.user_reads.count()


class ArticleFollowingResource(ModelResource):
    
    article = fields.ToOneField(ArticleResource, 'article')
    user = fields.ToOneField(UserResource, 'user')
    
    class Meta:
        queryset = ArticleFollowings.objects.all()
        resource_name = 'following'
        filtering = {
            'article': ALL,
            'user': ALL,
            'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }


class ArticleRatingResource(ModelResource):
    
    rating_article = fields.ToOneField(ArticleResource, 'article')
    rating_user = fields.ToOneField(UserResource, 'user')
    class Meta:
        resource_name = 'rating'
        queryset = ArticleRating.objects.all()
        


class CategoryResource(ModelResource):
    sub_categories = fields.ToManyField('blog.api.SubCategoryResource', 'sub_categories', related_name='sub_categories', full=True)
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
       


class SubCategoryResource(ModelResource):
    subcategory = fields.ToOneField(CategoryResource, 'catagory_id')
    class Meta:
        queryset = SubCategory.objects.all()
        resource_name = 'subcategory'
        allowed_methods = ['get']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
