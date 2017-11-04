# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from collections import OrderedDict
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views import View
from .forms import ArticleForm
from blog import Article, ArticleLikes
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.core.files.uploadedfile import SimpleUploadedFile
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from tracking_analyzer.models import Tracker
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.cache import cache_page
#  for comments 
from notifications.signals import notify
from django_comments.signals import comment_was_posted
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.views.generic.edit import CreateView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string


# homepage
def index(request):
    return render(request, 'index.html')


class CreateArticle(LoginRequiredMixin, CreateView):
    """
    """
    template_name = 'article_template.html'
    form_class = ArticleForm
    success_url = reverse_lazy('articles')

    def form_valid(self, form):
        import pdb
        pdb.set_trace()
        form.instance.article_author = self.request.user
        return super(CreateArticle, self).form_valid(form)


@login_required
@permission_required('blog.change_article', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method =='GET': 
        if request.user == article.article_author:
            form  = ArticleForm(instance=article)
            return render(request, 'article_template.html', {"form":form} )
        else:
            return HttpResponse('<h1>Error 403 Not Allowed</h1>')

    if request.method =='POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid() and form.is_multipart():
            article_instance = form.save(commit=False)
            article_instance.save()

    return render(request, 'article_template.html', {"form":form} )


def user_liked(user_id, article_id):
    try:
        if len(ArticleLikes.objects.filter(article_id=article_id, user_id=user_id)):
            return True
    except:
        return False


def BlogIndex(request, **kwargs):
    '''
    view for Homepage of blog
    '''
    
    # prepare for launching the jason data
    articles_json = []
    if request.method == "GET":

        query_set = Article.objects.all().order_by('-article_views',  '-created')
        paginator = Paginator(query_set, 15)
        page = request.GET.get('page')
        try:
            article_page = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            article_page = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            article_page = paginator.page(paginator.num_pages)
        context = {}
        for item  in article_page.object_list:
            articles_json.append({
                'article':item,
                "likes":item.count_likes(),
                "user_liked":user_liked(request.user.id, item.id)
                })
        popular_tags = Article.get_counted_tags()
        return render( request, 'gallery.html', {'popular_tags':popular_tags, 'article_page':article_page, 'articles_json': articles_json})


def ArticleView(request, pk):
    '''View for displaying the article on the page includes analytics '''
    article = get_object_or_404(Article, pk=pk, article_state='published')
    Tracker.objects.create_from_request(request, article)
    return render(request, 'article.html', {'tags':'', "article": article, "article_analytics": article_analytics(request)})


def article_analytics(request):
    query_set = Article.objects.order_by('-created')
    newest = query_set[0].created.year
    oldest = query_set.reverse()[0].created.year
    article_by_year = dict()
    for year in range(oldest, newest+1):
        try:
            temp = query_set.filter(created__year=year)
            article_by_year.update({year:{}})
            for month in range(1,13):
                by_month = temp.filter(created__month=month) 
                if by_month:
                    article_by_year[year].update({by_month[0].created:temp.filter(created__month=month)})
        except:
            pass
    return article_by_year


def article_preview(request):
    try:
        if request.method == 'POST':
            content = request.POST.get('content')
            html = 'Nothing to display :('
            if len(content.strip()) > 0:
                html = markdown.markdown(content, safe_mode='escape')

            return HttpResponse(html)

        else:   # pragma: no cover
            return HttpResponseBadRequest()

    except Exception:   # pragma: no cover
        return HttpResponseBadRequest()


@receiver(comment_was_posted)
def Rec(sender, **kwargs):
    user= kwargs.get('request').user
    comment = kwargs.get('comment')
    url = comment.get_content_object_url()
    commented_on = comment.content_object

    notify.send(user, recipient=commented_on.article_author, verb='%s Commented  %s on %s Article' %(comment.name, comment.comment,comment.content_object), comment_url=url)

@receiver(post_save, sender=Article)
def ArticleReciever(sender, **kwargs):
    import pdb
    pdb.set_trace()
    # notify.send(user, recipient=user, verb='you reached level 10')