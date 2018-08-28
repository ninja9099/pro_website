from django.contrib.auth.models import Group
from user_profile.models import User
from rest_framework import serializers
from blog.models import *

class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


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
    article_image = Base64ImageField(max_length=None)
    likes = ArticleLikesSerializer(source='articlelikes_set',  many=True, read_only=True)
    article_tags = serializers.PrimaryKeyRelatedField(queryset=ArticleTags.objects.all(), many=True)
    class Meta:
        model = Article
        fields = ('id','article_author', 'article_title', 'article_image', 'article_category','likes','article_tags', 'article_subcategory', 'article_content', 'article_author', 'article_state', 'article_slug')


    def to_internal_value(self, data):
        tags_to_add  = []
        try:
            for item in data.get('article_tags'):
                tag_attached, is_there = ArticleTags.objects.get_or_create(name=item.get('value'))
                tags_to_add.append(tag_attached.id)
        except:
            pass
        tags = tags_to_add
        data['article_tags'] = tags
        ret = super(ArticleSerializer, self).to_internal_value(data)
        return ret

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