# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . models import (MySelf, MyWork, CarouselImages, Services, Team,)
# Register your models here.




class MyWorkAdmin(admin.ModelAdmin):
    list_display = ['project_image',
                    'project_url',
                    'project_description',]
    list_display_links = ('project_description',)

class MySelfAdmin(admin.ModelAdmin):
    list_display = ['bio',
                    'location',
                    'birth_date',
                    'profile_picture',
                    'articles_authored',
                    'why_hire']

    def  articles_authored(self, obj):
        return len([p.article_title for p in obj.authored.all()])

class CarouselImagesAdmin(admin.ModelAdmin):
    list_display = [
        'image_name',
        'carousel_image_url',
        'is_active']

class ServicesAdmin(admin.ModelAdmin):
    list_display = [
        'service_name',
        'service_image',
        'service_description']

class TeamAdmin(admin.ModelAdmin):
    list_display = ['dev_name',
                    'dev_image',
                    'dev_exp',]



admin.site.register(MySelf, MySelfAdmin)
admin.site.register(MyWork, MyWorkAdmin)
admin.site.register(CarouselImages, CarouselImagesAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Team, TeamAdmin)