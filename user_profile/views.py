# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForm
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from . models import UserProfile
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def login(request):
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
                else:
                    form.add_error(None, "username or password in correct")
                    return render(request, 'registration/login.html', {'form': form})
                
                return  HttpResponseRedirect(reverse('homepage'))
    else:
        form = LoginForm()    # A empty, unbound form
    return render(request, 'registration/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('homepage'))



@login_required
def ManageProfile(request, profile_id):
    if request.method=='GET':
        UserProfile=User.objects.get(id=1).userprofile
        article_reads = UserProfile.article_reads.all()
        return render(request, 'registration/profile.html', {"UserProfile": UserProfile, "articles_written":len(request.user.article_set.all()),"article_reads":article_reads })