# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.urls import reverse
from .forms import LoginForm,UserProfileForm
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from . models import UserProfile

def index(request):
    return render(request, 'index.html')

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
    import pdb
    pdb.set_trace()
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
        form = LoginForm()    # A empty, unbound form
    return render(request, 'registration/login.html', {'form': form, "next":next_url})


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def sign_up(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            clean_form =form.cleaned_data
            import pdb
            pdb.set_trace()
    else:
        form = UserProfileForm()
    return render(request, 'registration/signup.html', {'form': form})
@login_required
def ManageProfile(request, profile_id):
    if request.method=='GET':
        userprofile= UserProfile.objects.get(user__id=profile_id)
        article_reads = userprofile.article_reads.all()
        return render(request, 'registration/profile.html', {"UserProfile": userprofile, "articles_written":len(request.user.article_set.all()),"article_reads":article_reads })