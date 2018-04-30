
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from blog.blog import Article
from serializers import ArticleSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@csrf_exempt
@api_view(['GET', 'POST'])
def article_list(request,  format=None):
    """
    List all code articles, or create a new article.
    """
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code article.
    """
    try:
        article = Article.objects.get(pk=pk)
    except article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)