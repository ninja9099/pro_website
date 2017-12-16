# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import json
import requests
import urllib2

from PIL import Image
from django.core.files import File
from urlparse import urlparse
from django.core.files.temp import NamedTemporaryFile
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, render_to_response,redirect
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse, Http404
from django.urls import reverse
from .forms import LoginForm,UserProfileForm
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from . models import UserProfile
from django.forms import ModelForm, Textarea
from django.views.generic.edit import UpdateView
from user_profile.forms import UserProfileForm, SignUpForm
from django.views.decorators.cache import cache_page
from django.dispatch import receiver
from django.db.models.signals import post_save


def user_details(strategy, details, response, user=None, *args, **kwargs):
    if user:
        if kwargs['is_new']:
            if kwargs.get('backend').__class__.__name__ == 'GoogleOAuth2':
                profile = UserProfile.objects.create(
                    user=user,
                    gender = response.get('gender'),
                    user_type=3,
                    )
                img_url = response.get('image').get('url')
                img_name = urlparse(img_url).path.split('/')[-1]
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(urllib2.urlopen(img_url).read())
                profile.profile_picture.save(img_name, File(img_temp))
                img_temp.flush()
                return True

            if kwargs.get('backend').__class__.__name__ == "FacebookOAuth2":
                profile = UserProfile.objects.create(
                    user=user,
                    gender = response.get('gender'),
                    user_type=3,
                    )
                img_url = response.get('picture').get('data').get('url')
                img_name = urlparse(img_url).path.split('/')[-1]
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(urllib2.urlopen(img_url).read())
                profile.profile_picture.save(img_name, File(img_temp))
                img_temp.flush()
                return True

            if kwargs.get('backend').__class__.__name__  == 'TwitterOAuth':
                profile = UserProfile.objects.create(
                    user=user,
                    user_type=3,
                    )
                img_url = response.get('profile_image_url')
                img_name = urlparse(img_url).path.split('/')[-1]
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(urllib2.urlopen(img_url).read())
                profile.profile_picture.save(img_name, File(img_temp))
                img_temp.flush()
                return True


def _login_ajax(request,username, password, remember):
    if username and password:
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            if remember:
                settings.SESSION_COOKIE_AGE = 24 * 365 * 3600
            if not request.POST.get('next'): # FIXME Find some  batter way to do this
                next_url = '/'
            return JsonResponse({'login':True,})
        else:
            return JsonResponse({"error":'Username or password is incorrect'})
    else:
        return JsonResponse({"error":'Username & password required'})

@csrf_exempt
def login(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/')
    
    if request.POST.get('is_ajax'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember_me')
        next_url = request.POST.get('next_url')
        return _login_ajax(request, username, password,remember)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            clean_form =form.cleaned_data
            username= clean_form.get('username')
            password = clean_form.get('password')
            remember = clean_form['remember_me']
            if username and password:
                user = authenticate(username=username, password=password)
                if user:
                    auth_login(request, user)
                    request.session['username'] = username
                    if remember:
                        settings.SESSION_COOKIE_AGE = 24 * 365 * 3600
                    if request.POST.get('next'): # FIXME Find some  batter way to do this
                        return HttpResponseRedirect(request.POST.get('next'))
                else:
                    form.add_error(None, "username or password in correct")
                    return render(request, 'registration/login.html', {'form': form})
                
                return  HttpResponseRedirect(reverse('homepage'))
        else:     
            return render(request, 'registration/login.html', {'form': form})
    else:
        next_url = request.GET.get('next') or '/'
        form = LoginForm() # A empty, unbound form
    return render(request, 'registration/login.html', {'form': form, "next":next_url})


def logout(request):
    auth_logout(request)
    
    return HttpResponseRedirect(reverse('homepage'))


def sign_up(request):
    if not request.user.is_anonymous():
        return redirect('homepage')

    if request.method == 'POST' :
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def edit_profile(request, profile_id):
    if request.method=='GET':
        if request.GET.get('edit', 'false') == 'false':
            article_reads = request.user.userprofile.article_reads.all()
            return render(request, 'registration/profile.html', {"articles_written":len(request.user.article_set.all()),"article_reads":article_reads })
        else:
            try:
                profile = UserProfile.objects.get(user__id=profile_id)
            except:
                raise Http404
            if request.user == profile.user:
                form = UserProfileForm(instance=profile)
                return render(request, 'userprofile_update_form.html', {'form': form})
            else:
                raise PermissionDenied

    if request.method == "POST":
        user_profile  = UserProfileForm(request.POST, request.FILES, instance=UserProfile.objects.get(pk=profile_id))
        if user_profile.is_valid():
            # user_profile.profile_picture=request.FILES['profile_picture']
            user_profile.save()
            return HttpResponseRedirect(reverse('profile', kwargs={'profile_id':request.user.id}))
        else:
            return render(request, 'userprofile_update_form.html', {'form': user_profile})


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs.get('created'):
        user_profile =UserProfile(user=kwargs.get('instance'), user_type=3)
        user_profile.save()
        return True
    else:
        pass


def social_auth(request):
   return redirect('homepage')
