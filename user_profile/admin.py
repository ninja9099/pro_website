# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, User
from .models import UserProfile, User

class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profiles'


class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']


admin.site.register(User)
