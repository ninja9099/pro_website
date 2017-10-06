import exceptions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializers import ArticleLikesSerializer
from blog.blog import ArticleLikes

from rest_framework.views import exception_handler

def rest_exc_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
    
    if isinstance(exc, exceptions.AssertionError):
        return Response('you did not liked this article yet', status=status.HTTP_404_NOT_FOUND)
    return response

@api_view(['GET', 'POST', 'DELETE'])
def article_likes(request, pk):
    """
    list all comments or pst a new comment if user is logged in anonymous posting is not allowed
    error codes :
        404 comment with supplied id not found in the base
        400 data invalid
    """
    try:
        article_likes = ArticleLikes.objects.filter(article_id=pk)
    except ArticleLikes.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        import pdb
        pdb.set_trace()
        serializer = ArticleLikesSerializer(article_likes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleLikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            like = ArticleLikes.objects.filter(article_id=pk, user_id=request.user)
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except like.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            