"""
Django settings for the dj project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from YamJam import yamjam
from django.core.urlresolvers import reverse_lazy

parms = yamjam()['dj']

LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('home')

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = parms['django-secret-key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = parms['debug']

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [parms['allowed-hosts']]


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'filebrowser',
    'tinymce',
    'taggit',
    'dbbackup',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'registration',
    'educate',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dj.urls'

WSGI_APPLICATION = 'dj.wsgi.application'

# For django-registration-redux
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True

EMAIL_HOST = parms['email-host']
EMAIL_PORT = parms['email-port']

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': parms['database-engine'],
        'NAME': parms['database-name'],
        'USER': parms['database-user'],
        'PASSWORD': parms['database-password'],
        'HOST': parms['database-host'],
        'PORT': parms['database-port'],
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, parms['static-root'])
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/grappelli'

# Base folder locations

STATIC_ROOT = os.path.join(BASE_DIR, parms['static-root'])
MEDIA_ROOT = os.path.join(BASE_DIR, parms['media-root'])

# Inline editor for articles

TINYMCE_JS_URL = parms['tinymce-js-url']
TINYMCE_JS_ROOT = parms['tinymce-js-root']
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_levels': 10,
    }
TINYMCE_COMPRESSOR = True
TINYMCE_SPELLCHECKER = True
