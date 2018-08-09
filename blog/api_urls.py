from django.conf import settings
from django.conf.urls import url, include
from api import (
	ArticleResource, 
	UserResource, 
	ArticleFollowingResource, 
	ArticleRatingResource,
	CategoryResource,
	SubCategoryResource,
	# HomePageResources,
	CommentResource,
	ArticleTagsResource
	)
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(ArticleResource())
v1_api.register(ArticleFollowingResource())
v1_api.register(ArticleRatingResource())
v1_api.register(CategoryResource())
v1_api.register(SubCategoryResource())
# v1_api.register(HomePageResources())
v1_api.register(CommentResource())
v1_api.register(ArticleTagsResource())

urlpatterns = [
    url(r'^', include(v1_api.urls)),
]
