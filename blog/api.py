
import json
import warnings
from tastypie import fields
from tastypie.resources import ModelResource, Resource, ALL, ALL_WITH_RELATIONS
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication,Authentication
from django.contrib.auth import authenticate
from django.http import HttpResponse
from tastypie.authorization import Authorization, DjangoAuthorization
from django.conf.urls import include, url
from django_comments.models import Comment
from django.core.paginator import (
    InvalidPage,
    Paginator
)
from tastypie.models import ApiKey
from django.contrib.auth import login
from django.conf import settings
from my_self.models import MySelf, MyWork,CarouselImages,Services,Team,CompanyInfo
from user_profile.models import User
from .models import (Article, 
    ArticleRating,
    ArticleFollowings,
    Category,
    SubCategory
)



class CommentResource(ModelResource):
    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'
        excludes = []
        allowed_methods = ['get']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = DjangoAuthorization()



def _get_parameter(request, name):
    '''
    Helper: abstraction to recover paremeters from POST or GET
    either
    '''

    if request.POST:
        try:
            return request.POST[name]
        except KeyError, e:
            # print e
            return None
    if request.GET:
        try:
            return request.GET[name]
        except KeyError as e:
            return None


class MySelfResource(ModelResource):
    
    class Meta:
        
        queryset = MySelf.objects.all()
        resource_name = 'myself'
        excludes = []
        allowed_methods = ['get']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = DjangoAuthorization()


class MyWorkResource(ModelResource):
    
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
   
    mywork = fields.ToManyField('blog.api.MyWorkResource','mywork',null=True)
    services = fields.ListField(null=True, blank=True)
    carousel_images = fields.ListField(null=True, blank=True)

    class Meta:
        queryset = MySelf.objects.all()
        resource_name = 'main'
        allowed_methods = ['get']
        authorization = DjangoAuthorization()
        authentication = ApiKeyAuthentication()

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/index$" % self._meta.resource_name,
                self.wrap_view('index'), name="landing_gear")
        ]

    def dehydrate_carousel_images(self, bundle):
        return list(CarouselImages.objects.all().values_list('carousel_image_url', flat=True))

    def dehydrate_services(self, bundle):
        return list(Services.objects.all().values_list('service_name','service_image', 'service_description'))

    def index(self, request, *args, **kwargs):
        
        self.method_check(request, allowed=['get'])
        self.is_authenticated(request)
        self.throttle_check(request)

        article_res = ArticleResource(api_name='v1')
        page_offset = _get_parameter(request, 'offset')
        page_limit = _get_parameter(request, 'limit')
        article_limit = _get_parameter(request, 'article_limit')

        object_list = []

        popular_articles = Article.objects.filter(article_state="published").order_by('-modified')
        paginator = Paginator(popular_articles, int(page_limit))
        
        try:
            page = paginator.page(1)
        except InvalidPage:
            raise Http404("Sorry, no results on that page.")    

        article_bundle = []
        for article in popular_articles:
            bundle = article_res.build_bundle(obj=article, request=request)
            bundle = article_res.full_dehydrate(bundle)
            article_bundle.append(bundle)

        object_list = {
            'articles': article_bundle,
        }
        self.log_throttled_access(request)
        return self.create_response(request, object_list)


class UserResource(ModelResource):
    
    articles_authored = fields.ToManyField('blog.api.ArticleResource', 'article_written', related_name='article_written')
    comments = fields.ListField(attribute='get_all_comments', readonly=True)
    full_name = fields.CharField(attribute="get_full_name", readonly=True)
    article_reads = fields.ListField(attribute='get_article_reads', readonly=True)
    profile_picture = fields.CharField(attribute='get_profile_image', readonly=True)
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        allowed_methods = ['get']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = ApiKeyAuthentication()
        always_return_data = True
        # authorization = DjangoAuthorization()

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/login$" % self._meta.resource_name,
                self.wrap_view('login'), name="login")
        ]
    def login(self, request, *args, **kwargs):
        data = json.loads(request.body)
        username = data.get('user')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        res = {}
        if user is not None:
            if user.is_active:
                login(request, user)
                try:
                    apikey = ApiKey.objects.get(user=user).key
                except Exception as e:
                    print str(e)
                    warnings.warn("Your API key is not available\n Contact Admin at" + settings.EMAIL_ADMIN + \
                    'to generate api key')

                    res = {'is_authenticated': False, 'message': "Your API key is not available \n \
                    Contact Admin at" + settings.EMAIL_ADMIN + \
                    'to generate api key'}
                else:
                    user_res = UserResource(api_name='v1')
                    bundle = user_res.build_bundle(obj=user, request=request)
                    bundle = user_res.full_dehydrate(bundle)
                    res.update({'user': user,'user_resource':bundle, 'is_authenticated': True, 'message': 'Login successful', 'apikey': apikey })  
        else:
            res = {'is_authenticated': False, 'message': 'Please Check your Credentials :)'}
        self.log_throttled_access(request)
        return self.create_response(request, res)

class ArticleResource(ModelResource):
    
    author = fields.ForeignKey(UserResource, 'article_author', full=True)
    # article_tags = fields.ToManyField( 'tags',  full=True)
    article_image = fields.CharField(attribute='get_article_image', readonly=True, null=True, blank=True)
    follow_list = fields.ListField(null=True, blank=True)
    total_rating = fields.FloatField()
    likes = fields.ListField(attribute='get_likes', readonly=True)
    comments = fields.ToManyField('blog.api.CommentResource', 'article_comments',blank=True,null=True, full=True)
    total_reads = fields.IntegerField(default=0, blank=True)
    article_category = fields.ForeignKey('blog.api.CategoryResource', 'article_category', full=True)
    article_subcategory = fields.ForeignKey('blog.api.SubCategoryResource', 'article_subcategory', full=True)
    class Meta:
        queryset = Article.objects.filter(article_state="published")
        resource_name = 'article'
        filtering = {   
            'slug': ALL,
            'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
        
        allowed_methods = ['get','post']
        authentication= Authentication()
        authorization = Authorization()
    

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
    category = fields.ToOneField(CategoryResource, 'catagory_id')  
    class Meta:
        queryset = SubCategory.objects.all()
        resource_name = 'subcategory'
        allowed_methods = ['get']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'catagory_id': ['exact']
        }