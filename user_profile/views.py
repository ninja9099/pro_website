# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login, logout
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')
        if authenticate(username=user, password=password):
            login(user, password)
        else:
            return render('user_profile/login.html')
    else:
        return render('user_profile/index.html', {})

def index(request):
    ## ---> Set BreakPoint
    import pdb;
    pdb.set_trace()
    return HttpResponse('Hello World')

def logout(request):
    return HttpResponse()