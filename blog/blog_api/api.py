from .blog import Article
from django.contrib.auth.models import AnonymousUser, User


def get_article(requesting_user, article_ids=[]):
	Article.objects.get()