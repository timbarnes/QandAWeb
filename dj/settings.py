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
from django.urls import reverse_lazy

parms = yamjam()['dj']

LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('home')

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

print(os.path.join(BASE_DIR, 'templates'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = parms['django-secret-key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = parms['debug']

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [parms['allowed-hosts']]

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj.settings")

# Application definition

INSTALLED_APPS = (
    'tinymce',
    'taggit',
    'crispy_forms',
    'dbbackup',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'users',
    'registration',
    'educate',
)

if DEBUG:
    INSTALLED_APPS = ('debug_toolbar',) + INSTALLED_APPS

MIDDLEWARE = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
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

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Base folder locations
# STATIC_FILES_DIRS = os.path.join(BASE_DIR, parms['static-dir'])
STATIC_ROOT = os.path.join(BASE_DIR, parms['static-root'])
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, parms['media-root'])

# Inline editor for articles

# TINYMCE_JS_URL = parms['tinymce-js-url']
# TINYMCE_JS_ROOT = parms['tinymce-js-root']
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_levels': 10,
    }
TINYMCE_COMPRESSOR = True
TINYMCE_SPELLCHECKER = True
