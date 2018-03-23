from rest_framework import serializers
from blog.blog import ArticleLikes, Article
from taggit.models import Tag
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

class ArticleLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleLikes
        fields = ('user_id', 'article_id')

class ArticleSerializer(TaggitSerializer, serializers.ModelSerializer):
	tags = TagListSerializerField()
	class Meta:
		model = Article
		fields = ('__all__')


