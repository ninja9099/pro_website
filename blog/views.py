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
from django.db.models.query_utils import  Q
from django.db import models
from django.db.models.constants import LOOKUP_SEP
from rest_framework.views import APIView
from blog.aws import upload_to_s3
from rest_framework.renderers import JSONRenderer



User = get_user_model()


def build_filters(queryset, query_params):
    filters= {}
    model = queryset.model
    field_names = [f.name for f in model._meta.get_fields()]
    
    for filter_expr, value in query_params.items():
        filter_bits = filter_expr.split(LOOKUP_SEP)
        field_name = filter_bits.pop(0)
        
        if field_name not in field_names:
            # It's not a field we know about. Move along citizen.
            continue
        field_instance = model._meta.get_field(field_name)

        if hasattr(field_instance, '_related_fields'):
            rel_fields = [f.name for f in field_instance.related_fields[0]]

            if filter_bits:
                lookup = filter_bits.pop()
                if lookup in rel_fields:
                    filters.update({filter_expr: value})
                else:
                    continue
            else:
                filters.update({filter_expr: value})
        else:
            filters.update({filter_expr: value})

    query_set = queryset.filter(Q(**filters))
    return query_set
        


    


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
    queryset = build_filters(queryset, request.query_params)
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
    queryset = build_filters(queryset, request.query_params)
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
    queryset = Category.objects.all()
    queryset = build_filters(queryset, request.query_params)
    if request.method == 'GET':
        serializer = CategorySerializer(queryset, many=True)
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
def subcategory_list(request):
    """
    List all code Articles, or create a new Article.
    """
    cat_id = request.query_params.get('catagory_id', None)
    queryset = SubCategory.objects.all()
    queryset = build_filters(queryset, request.query_params)
    if request.method == 'GET':
        serializer = SubCategorySerializer(queryset, many=True)
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
def like_list(request):
    """
    List all code Articles, or create a new Article.
    """


    queryset = ArticleLikes.objects.all()
    queryset = build_filters(queryset, request.query_params)
    if request.method == 'GET':
        serializer = ArticleLikesSerializer(queryset, many=True)
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
def user_list(request):
    """
    List all code Articles, or create a new Article.
    """
    queryset = User.objects.all()
    queryset = build_filters(queryset, request.query_params)
    if request.method == 'GET':
        serializer = UserSerializer(queryset, many=True)
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
        return Response(serializer.data)

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


class EditoreUploadImage(APIView):

    renderer_classes = (JSONRenderer, )
    def get(self, request, *args, **kw):
        import pdb
        pdb.set_trace()
        pass

    def post(self, request, *args, **kw):
        import pdb; pdb.set_trace()
        key = 'article-images/' + request.FILES['file'].name
        files = request.FILES['file']
        url = upload_to_s3(files, key)
        res = {"link": url}
        return Response(res)
        
