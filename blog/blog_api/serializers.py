from rest_framework import serializers
from blog.blog import ArticleLikes


class ArticleLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleLikes
        fields = ('user_id', 'article_id')
