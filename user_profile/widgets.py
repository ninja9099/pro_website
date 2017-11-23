# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.forms.widgets import Widget
from django.template import loader
from django.utils.safestring import mark_safe
from django.forms.utils import flatatt
from django.forms.widgets import ClearableFileInput


class ProfilePicWidget(ClearableFileInput):
    template_name = 'profilePic.html'
    def __init__(self, attrs):
        super(ProfilePicWidget, self).__init__(attrs)
        print attrs
        self.attrs = attrs.copy()

    def get_context(self, name, value, attrs=None):
        return {'widget': {
            'name': name,
            'value': value,
            'attrs':attrs,
        }}

    def render(self, name, value, attrs=None):
        print attrs
        flat_attrs = flatatt(attrs)
        context = self.get_context(name, value, flat_attrs)
        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)