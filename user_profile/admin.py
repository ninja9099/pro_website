# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, User
from .models import UserProfile, User


admin.site.register(User)