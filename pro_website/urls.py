"""pro_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from user_profile import views
from user_profile import views as custom_auth_views
from blog import blog, views as article_views
from django.conf.urls import (handler400, handler403, handler404, handler500)

urlpatterns = [
    
    url(r'^$', views.index, name='homepage'),
    url('', include('social_django.urls', namespace='social')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', custom_auth_views.login, name='login'),
    url(r'^logout/$', custom_auth_views.logout, name='logout'),
    url(r'^sign-up/$', custom_auth_views.sign_up, name='sign-up'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^profile/(?P<profile_id>[0-9]*)$', custom_auth_views.ManageProfile, name='profile'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^blog/', include('blog.urls'),  name="blog"),
    url(r'^article-list/$', article_views.ArticleListView.as_view(),  name='article-list'),
    url(r'^tracking/', include('tracking.urls')),
    url(r'^complete/social-oauth2$',custom_auth_views.social_auth, name="social_auth")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'blog.errorhandler.handler404'
handler500 = 'blog.errorhandler.handler500'
handler403 = 'blog.errorhandler.handler403'