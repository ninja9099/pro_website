# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.functional import cached_property
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from blog.aws import upload_to_s3


PROFILE_PIC_PATH = settings.IMAGE_PATH + 'profile_images/'

user_type_choices = [(1, 'Admin'), (2, 'Moderator'), (3, 'Normal')]
default_image = settings.DEFAULT_USER_IMAGE

class social_network(models.Model):
    user_id = models.ForeignKey('User', related_name='social_networks')
    site_name = models.CharField(max_length=255)
    account = models.CharField(
        max_length=255, help_text="please insert only id of your account")


class User(AbstractUser):

    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to=PROFILE_PIC_PATH, default=default_image,blank=True)
    self_intro = models.CharField(max_length=255, blank=True)
    _s3_image_path = models.URLField(max_length=1000, blank=True)
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @cached_property
    def get_all_comments(self):
        return list([item for item in self.comment_comments.all()])

    def get_full_name(self):
        if self.first_name:
            return "{0} {1}".format(self.first_name, self.last_name)
        else:
            return "{0}".format(self.username)

    def get_profile_image(self):
        """
        get profile image for the user and if not found returns  the 
        default images
        """
        try:
            return self.profile_picture
        except AttributeError:
            return settings.DEFAULT_USER_IMAGE

    def save(self, *args, **kwargs):
        url = upload_to_s3(self.profile_picture, self.profile_picture.name)
        self._s3_image_path = url
        super(User, self).save(*args, **kwargs)



@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
