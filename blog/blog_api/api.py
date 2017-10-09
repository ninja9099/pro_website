import exceptions
from rest_framework import status
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.response import Response
from serializers import ArticleLikesSerializer
from blog.blog import ArticleLikes
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler
from rest_framework.renderers import JSONRenderer

class NotAllowedError(APIException):
    status_code = 504
    default_detail = 'your are not allowed to do the work of others.'
    default_code = 'fraudulant '

def rest_exc_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
        if response.status_code == 403:
            response.data = {'error':'please login to proceed','error_code':403}
        elif response.status_code == 400:
            response.data = {'error':'server error please try after refreshing page','error_code':400}
        elif response.status_code == 404:
            response.data = {'error':'you did not liked this article yet','error_code':404}
    
    if isinstance(exc, exceptions.AssertionError):
        print(exc.detail())

    return response

@api_view(['GET', 'POST', 'DELETE'])
@renderer_classes((JSONRenderer,))
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
        serializer = ArticleLikesSerializer(article_likes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if int(request.data.get('user_id')) == request.user.id:
            serializer = ArticleLikesSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                content = {'total_likes':len(ArticleLikes.objects.filter(article_id=pk))}
                return Response(content, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            # return Response(status=status.HTTP_400_BAD_REQUEST)
            raise NotAllowedError()
    
    elif request.method == 'DELETE':
        if int(request.data.get('user_id')) == request.user.id:
            try:
                like = ArticleLikes.objects.filter(article_id=pk, user_id=request.user)
                like.delete()
                content = {'total_likes':len(ArticleLikes.objects.filter(article_id=pk))}
                return Response(content, status=status.HTTP_201_CREATED)
            except :
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            raise NotAllowedError()