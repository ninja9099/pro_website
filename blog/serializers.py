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


class ArticleSerializer():
    class Meta:
        model = Article
        fields = ('article_title', 'article_image', 'article_category', 'article_subcategory', 'article_content', 'article_author', 'article_state', 'article_slug', 'article_tags')
