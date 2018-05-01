from tastypie.resources import ModelResource
from blog import Article


class ArticleResource(ModelResource):
    class Meta:
        queryset = Article.objects.all()
        resource_name = 'article'
        