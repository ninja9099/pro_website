# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import markdown
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views import View
from .forms import ArticleForm
from blog import Article, ArticleLikes
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseBadRequest,JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.core.urlresolvers import reverse_lazy
from tracking_analyzer.models import Tracker
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#  for comments
from notifications.signals import notify
from django_comments.signals import comment_was_posted
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.urls import reverse
from blog_api import core


# homepage
def index(request):
    context = core.create_context(request)
    fresh = context.get('article_set').latest('created')
    context.push({'fresh_article': fresh})
    return render(request, 'index.html', {"context": context})


@login_required
def create_article(request):
    if request.method=="GET":
        form = ArticleForm()

    if request.is_ajax() and request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article_instance = form.save(commit=False)
            article_instance.article_state = "draft"
            article_instance.article_author = request.user
            article_instance.save()
            form.save_m2m()
            return JsonResponse({'success':True, 'message':'Your article\
             is saved at <a href="/blog/article_edit/{}">here</a>'.format(article_instance.id)})
        else:
            return JsonResponse({"success":False, "error":render_to_string('errors.html', {'form':form})})

    return render(request, 'article_template.html', {"form":form, 'url':reverse('article_submit')})


@login_required
@permission_required('blog.change_article', raise_exception=True)
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method =='GET':
        if request.user == article.article_author:
            form  = ArticleForm(instance=article)
            return render(request, 'article_template.html', {"form":form, 'url':reverse('article_edit', kwargs={'pk':article.id})})
        else:
            return HttpResponse('<h1>Error 403 Not Allowed</h1>')

    if request.method =='POST' and request.is_ajax():
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid() and form.is_multipart():
            # core.handle_uploaded_file(request.FILES['file'],  type='article') for future use 
            # article_instance.article_image = request.FILES['file'][0]
            article_instance = form.save(commit=False)
            article_instance.save()
            form.save_m2m()
            if article_instance.article_state == "published":
                notify.send(article_instance.article_author, recipient=User.objects.all(), verb="New article by %s"%(article_instance.article_author))
            return JsonResponse({'success':True, 'message':'Your article is saved'})
        else:
            return JsonResponse({'success':False, "error":render_to_string('errors.html', {'form':form})})


def user_liked(user_id, article_id):
    try:
        if ArticleLikes.objects.get(article_id=article_id, user_id=user_id).count():
            return True
    except:
        return False


def _paginate(query_set, obj_per_page, page):
    paginator = Paginator(query_set, obj_per_page)
    try:
        article_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        article_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        article_page = paginator.page(paginator.num_pages)

    return article_page


def BlogIndex(request, **kwargs):
    """
    view for Homepage of blog
    """
    if request.method == "GET":
        query_set = Article.get_published().order_by('-article_views',  '-created')
        page_no = request.GET.get('page')
        page = _paginate(query_set,3, page_no)
        context = core.create_context(request)
        context.push({'page':page})
        return render( request, 'gallery.html', {'context':context})


def article_view(request, pk):
    """
    View for displaying the article on the page includes analytics
    """

    article = get_object_or_404(Article, pk=pk, article_state='published')
    Tracker.objects.create_from_request(request, article)
    popular_tags = Article.get_counted_tags()
    recent = Article.get_published().order_by('-created').exclude(id=article.id)[:7]
    related_articles = Article.get_published().filter(article_subcategory=article.article_subcategory).exclude(id=article.id)[:5]
    if request.user.is_authenticated:
        request.user.userprofile.article_reads.add(article);
    return render(request, 'article.html', {
        'popular_tags': popular_tags,
        'article': article,
        'recent': recent ,
        'article_analytics': core.article_analytics(request, Article.objects.all()),
        'related_articles': related_articles,
        })

@login_required
def article_preview(request):
    try:
        if request.method == 'POST':
            content = request.POST.get('article_content')
            html = 'Nothing to display :('
            if len(content.strip()) > 0:
                html = markdown.markdown(content, safe_mode='escape')

            return HttpResponse(html)

        else:   # pragma: no cover
            return HttpResponseBadRequest()

    except Exception:   # pragma: no cover
        return HttpResponseBadRequest()


def tag(request, tag_name):
    context = core.create_context(request)
    query_set = Article.objects.filter(tags__name=tag_name).filter(article_state='published')
    page = _paginate(query_set, 3, request.GET.get('page'))
    context.push({'page': page})
    return render(request, 'tagged_articles.html',{'tag_name':tag_name, 'context':context} )


def category_view(request, cat_id):
    query_set = Article.objects.filter(id=cat_id)
    page_no = request.GET.get('page')
    page = _paginate(query_set, 3, page_no)
    context = core.create_context(request)
    context.push({'page':page})
    return render(request,'cat_article_list.html', {'context': context})


# TDME  move to core part  in the blog api
@receiver(comment_was_posted)
def Rec(sender, **kwargs):
    user= kwargs.get('request').user
    comment = kwargs.get('comment')
    url = comment.get_content_object_url()
    commented_on = comment.content_object
    if user.is_authenticated:
        notify.send(user,recipient=commented_on.article_author, target=commented_on, verb='Commented On', comment_url=url)
    else:
        pass


@receiver(post_save, sender=Article)
def ArticleReciever(sender, **kwargs):
    # user = kwargs.get('request').user
    # notify.send(user, recipient=user, verb='you reached level 10')
    pass
