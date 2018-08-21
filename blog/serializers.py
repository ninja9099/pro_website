from django.contrib.auth.models import Group
from user_profile.models import User
from rest_framework import serializers
from blog.models import *


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id','url', 'username', 'email')
        exclude = ('password', 'groups',  'user_permissions' )

class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = ('url', 'name')


class ArticleLikesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleLikes
        fields = ('id','user_id', 'article_id', 'is_liked')


class ArticleTagsSerializer(serializers.ModelSerializer):
    tagged_articles = serializers.StringRelatedField(many=True)

    class Meta:
        model = ArticleTags
        fields = ('id','name', 'slug', 'tagged_articles')

class ArticleSerializer(serializers.ModelSerializer):
    likes = ArticleLikesSerializer(source='articlelikes_set',  many=True)
    tags = ArticleTagsSerializer(source="article_tags", many=True)
    class Meta:
        model = Article
        fields = ('id','article_author', 'article_title', 'article_image', 'article_category','likes','tags', 'article_subcategory', 'article_content', 'article_author', 'article_state', 'article_slug')

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('id','category_name', 'category_image')


class SubCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubCategory
        fields = ('id','category_name', 'catagory_id',)


class ArticleRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model= ArticleRating
        fields = ('id','user', 'article', 'article_ratings', 'feedbacks')