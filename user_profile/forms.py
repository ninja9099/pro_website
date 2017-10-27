# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.admin import widgets       
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm

years = range(1991, 2017)
gender_choices = [('male', 'Male'), ('female', 'Female'),('notspecified', 'Dont Specify')]

class LoginForm(forms.Form):

    username = forms.CharField(error_messages={'required': 'username is required'}, required=True,label='Login Id', max_length=100, help_text="id to login in the system ie. John_Doe")
    password = forms.CharField(error_messages={'required': 'password is required'}, required=True, label='Password', widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False, label='Remember Me on this device', widget=forms.CheckboxInput)
    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError(_('User "%s" Not Found.' % username))
        return username

class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
    
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.filter(email=email)
        except User.DoesNotExist:
            pass
            
        if user:
            raise forms.ValidationError(_('User with email  "%s" already exists.' % email))
        return email


class UserProfileForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=years))
    mobile = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model=UserProfile
        fields = [
            'profile_picture',
            'birth_date',
            'address',
            'mobile',
            'gender',
            'about_me',
        ]
        widgets = {
            'address': Textarea(attrs={'cols': 80, 'rows': 2, 'class':'form-control'}),
            'about_me': Textarea(attrs={'cols': 80, 'rows': 2, 'class':'form-control'}),

        }



