"""
Django settings for Syndic project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from django.contrib.messages import constants as messages
import os
from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--dhvqb5l)7%)=^y8fmodpdb_v1%$5tf%=yyu9feu1g_n&ague0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
JAZZMIN_SETTINGS = {
    "site_title": "Admin Dashbord",
    "site_header": "Admin Dashbord",
    "site_brand": "Admin Dashbord",
    "site_icon": "img/logo_site.png",
    "site_logo":"img/logo_site.png",
     "login_logo": "img/logo_site.png",
     "login_logo_classes": "img-circle",
      "welcome_sign": "Welcome Admin",
      "show_sidebar": True,
      "navigation_expanded": True,




}
INSTALLED_APPS = [
    'crispy_bootstrap5',
    'authentication.apps.AuthenticationConfig',
    'Resident.apps.ResidentConfig',
    'crispy_forms',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'multiselectfield',
     'channels',

     
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Syndic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Syndic.wsgi.application'
ASGI_APPLICATION = 'Syndic.asgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.mysql', 
        'NAME'    : 'DjangoDB',                 
        'USER'    : 'root',                    
        'PASSWORD': 'xxxx',             
        'HOST'    : 'localhost',               
        'PORT'    : '3306',
    }
}
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER="smartlivingservice@gmail.com"
EMAIL_HOST_PASSWORD = 'xxxxxxxxx'
EMAIL_USE_TLS = True

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,'Syndic/static')]
STATIC_ROOT=os.path.join(BASE_DIR,'static')
MEDIA_URL="/media/"
MEDIA_ROOT=os.path.join(BASE_DIR,"media/")
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = 'Resident'
LOGIN_URL = "login"
MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
}

TWILIO_ACCOUNT_SID = 'xxx'
TWILIO_AUTH_TOKEN = 'xx'
TWILIO_PHONE_NUMBER = '+xx'

