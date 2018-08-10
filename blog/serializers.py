from django.contrib.auth.models import Group
from user_profile.models import User
from rest_framework import serializers
from blog.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('article_title', 'article_image', 'article_category', 'article_subcategory', 'article_content', 'article_author', 'article_state', 'article_slug', 'article_tags')

class ArticleTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTags
        fields = ('name', 'slug')

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('category_name', 'category_image')


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = ('category_name', 'catagory_id')


class ArticleLikesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleLikes
        fields = ('user_id', 'article_id', 'is_liked')


class ArticleRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model= ArticleRating
        fields = ('user', 'article', 'article_ratings', 'feedbacks')