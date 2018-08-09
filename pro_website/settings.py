"""
Django settings for pro_website project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tu5euh-)*w$=8k(g#i0ltr7ogrl)pd6)kr!j3@_wv!&2oz-8ne'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
LOGIN_URL = '/login/'
AUTH_USER_MODEL = 'user_profile.User'
# Application definition
EMAIL_ADMIN = "kamanipankaj9099@gmail.com"


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'blog',
    'user_profile',
    'django_comments',
    'tastypie',
    'tracking',
    'social_django',
    'tracking_analyzer',
    'django_user_agents',
    'notifications',
    'taggit',
    'autoslug',
    'corsheaders',
    'my_self',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'tracking.middleware.VisitorTrackingMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]

ROOT_URLCONF = 'pro_website.urls'

ADMIN_TITLE = "lifeinaBits - Admin"

TEMPLATES = [
    {   
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {    
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
            'debug': True,
        },
    },
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

WSGI_APPLICATION = 'pro_website.wsgi.application'

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
NOTIFICATION_TEST = True
NOTIFICATIONS_USE_JSONFIELD = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test2',
        'USER': 'lifeinabits',
        'PASSWORD': 'life@bits',
        'HOST': 'localhost',
        'PORT': '',
    }
}


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 10,

}


# auth backends
AUTHENTICATION_BACKENDS = (
    
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.yahoo.YahooOpenId',
    'django.contrib.auth.backends.ModelBackend',
)

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SOCIAL_AUTH_PIPELINE = (
        'social.pipeline.social_auth.social_details',
        'social.pipeline.social_auth.social_uid',
        'social.pipeline.social_auth.auth_allowed',
        'social.pipeline.social_auth.social_user',
        'social.pipeline.user.get_username',
        'social.pipeline.user.create_user',
        'social.pipeline.social_auth.associate_user',
        'social.pipeline.social_auth.load_extra_data',
        'social.pipeline.user.user_details',
        'user_profile.views.user_details'
    )

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')


MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')

MEDIA_URL = '/media/'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '521839123051-vgpj873gn87j9ir3vc765dqdpeu8um58.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'iDcr-og5VGFy4Bo8Pd2tygpT'

SOCIAL_AUTH_TWITTER_KEY = 'btuyBkzwuqHtMGJ52dnWdYOUw'
SOCIAL_AUTH_TWITTER_SECRET = 'WEPvHzGOWOSxet426Cxk7r2PYeRmrPi6ja64rkXDwsCcYiAUAa'

SOCIAL_AUTH_FACEBOOK_KEY = '181505989085886'
SOCIAL_AUTH_FACEBOOK_SECRET = '1ce4c5145bf9de326589dd2f9a9f9177'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'fields': 'id, name, email, age_range, gender, picture'
}


# settings related to article
# override to change default image of article
DEFAULT_ARTICLE_IMAGE = '/media/images/article_images/default.png'
DEFAULT_USER_IMAGE = '/media/images/profile_images/default_user.png'

#  for storing images and videos related to article 
IMAGE_PATH = 'images/'
VIDEO_PATH = 'videos/'

TAGGIT_CASE_INSENSITIVE = True

# google map integration for traffic tracking
TRACK_USE_GEOIP =True

GEOIP_CACHE_TYPE = 0
GEOIP_PATH =os.path.join(BASE_DIR, 'static/geoip-data/')

DEFAULT_TRACKING_TEMPLATE = 'tracking/visitor_map.html'

# django-tracking2 settings
TRACK_AJAX_REQUESTS =True
TRACK_ANONYMOUS_USERS =True
TRACK_PAGEVIEWS =True

TRACK_IGNORE_STATUS_CODES = [400, 404, 403, 405, 410, 500]
TRACK_REFERER =True
TRACK_QUERY_STRING= True

# notifications settings
NOTIFICATIONS_SOFT_DELETE=True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'kamanipankaj9099@gmail.com'
EMAIL_HOST_PASSWORD = 'mitalghadiya'

SUMMERNOTE_CONFIG = { 'width': '100%',  'height': '480',}
CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = (
    'google.com',
    'hostname.example.com',
    'localhost:8000',
    '127.0.0.1:9000'
)
