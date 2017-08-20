# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import collections
import copy
import datetime
import decimal
import itertools
import uuid
import warnings
from base64 import b64decode, b64encode
from functools import total_ordering

from django import forms
from django.apps import apps
from django.conf import settings
from django.core import checks, exceptions, validators
from django.core.exceptions import FieldDoesNotExist  # NOQA
from django.db import connection, connections, router
from django.db.models.constants import LOOKUP_SEP
from django.db.models.query_utils import DeferredAttribute, RegisterLookupMixin
from django.utils import six, timezone
from django.utils.datastructures import DictWrapper
from django.utils.dateparse import (
    parse_date, parse_datetime, parse_duration, parse_time,
)
from django.utils.deprecation import (
    RemovedInDjango20Warning, warn_about_renamed_method,
)
from django.utils.duration import duration_string
from django.utils.encoding import (
    force_bytes, force_text, python_2_unicode_compatible, smart_text,
)
from django.utils.functional import Promise, cached_property, curry
from django.utils.ipv6 import clean_ipv6_address
from django.utils.translation import ugettext_lazy as _


image_path = 'static/blog/article_image'
# Create your models here.
class Article(models.Model):
	article_title = models.CharField(max_size=255, db_index=True,help_text="please provide title of your article", unique=True)
	article_image = models.ImageField(upload_to=image_path, height_field=None, width_field=None)
	article_category = models.ForeignKey(Category, on_delete=models.CASCADE)
	article_subcategory models.ForeignKey(SubCategory, on_delete=models.CASCADE)
	article_followed = models.IntegerField(default=0)
	article_ratings = models.FloatField(default=0.0, blank=True)
	article_views =models.IntegerField(default=0)
	article_content = models.TextField()


class Category(models.Model):
	category_name = models.Charfield(max_size=255, unique=True)
