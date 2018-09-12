from django.contrib.auth.models import Group
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth import get_user_model
from blog.models import Article, ArticleTags, Category, ArticleLikes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from blog.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.conf import settings
from rest_framework.settings import api_settings
from user_profile.models import User

User = get_user_model()

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'is_authenticated': True, 'token': token.key, 'id': token.user_id, 'user': token.user.username })


@csrf_exempt
@api_view(['GET', 'POST'])
def article_list(request):
    """
    List all code Articles, or create a new Article.
    """
    
    queryset = Article.objects.all()
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    paginator = pagination_class()
    page = paginator.paginate_queryset(queryset, request)
    if request.method == 'GET':
        serializer = ArticleSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print  serializer.errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    


@csrf_exempt
@api_view(['GET', 'POST', 'PUT'])
def article_detail(request, pk):
    """
    Retrieve, update or delete a code Article.
    """
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'POST'])
def tag_list(request):
    """
    List all code Articles, or create a new Article.
    """

    queryset = ArticleTags.objects.all()
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    paginator = pagination_class()
    page = paginator.paginate_queryset(queryset, request)
    
    if request.method == 'GET':
        serializer = ArticleTagsSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST', 'PUT'])
def tag_detail(request, pk):
    """
    Retrieve, update or delete a code Article.
    """
    try:
        tag = ArticleTags.objects.get(pk=pk)
    except ArticleTags.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleTagsSerializer(tag)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleTagsSerializer(tag, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'POST'])
def category_list(request):
    """
    List all code Articles, or create a new Article.
    """
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST', 'PUT'])
def category_detail(request, pk):
    """
    Retrieve, update or delete a code Article.
    """
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'POST'])
def subcategory_list(request, cat_id=None):
    """
    List all code Articles, or create a new Article.
    """
    cat_id = request.query_params.get('catagory_id', None)

    if request.method == 'GET':
        if cat_id:
            subcategory = SubCategory.objects.filter(catagory_id=cat_id)
        else:
            subcategory = SubCategory.objects.all()
        serializer = SubCategorySerializer(subcategory, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SubCategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST', 'PUT'])
def subcategory_detail(request, pk):
    """
    Retrieve, update or delete a code Article.
    """
    try:
        subcategory = SubCategory.objects.get(pk=pk)
    except SubCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(subcategory)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SubCategorySerializer(subcategory, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        subcategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'POST'])
def like_list(request, article_id=None):
    """
    List all code Articles, or create a new Article.
    """
    like_id = request.query_params.get('article_id', None)

    if request.method == 'GET':
        if like_id:
            like = ArticleLikes.objects.filter(article_id=like_id)
        else:
            like = ArticleLikes.objects.all()
        serializer = ArticleLikesSerializer(like, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleLikesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST', 'PUT'])
def like_detail(request, article_id):
    """
    Retrieve, update or delete a code Article.
    """
    try:
        like = ArticleLikes.objects.get(article_id=article_id)
    except ArticleLikes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleLikesSerializer(like)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleLikesSerializer(like, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'POST'])
def user_list(request, user_id=None):
    """
    List all code Articles, or create a new Article.
    """
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'POST', 'PUT'])
def user_detail(request, user_id):
    """
    Retrieve, update or delete a code Article.
    """
    
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        import pdb
        pdb.set_trace()
        from django.http import HttpResponse, JsonResponse
        return JsonResponse(serializer.data, status=201)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        User.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
