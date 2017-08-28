# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class LoginForm(forms.Form):

	username = forms.CharField(required=True,label='Login Id', max_length=100, help_text="id to login in the system ie. John_Doe")
	password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput)
	remember_me = forms.BooleanField(required=False, label='Remember Me on this device', widget=forms.CheckboxInput)
	
	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			raise forms.ValidationError(_('User "%s" Not Found.' % username))
		return username

	def clean(self):
		pass


class UserProfileForm(forms.ModelForm):
	class Meta:
		model=UserProfile
		fields = ['user',
			'profile_picture',
			'birth_date',
			'address',
			'mobile',
			'user_type',
			'is_active',
		]