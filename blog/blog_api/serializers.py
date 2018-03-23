from rest_framework import serializers
from blog.blog import ArticleLikes, Article

class ArticleLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleLikes
        fields = ('user_id', 'article_id')

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = ('__all__')
