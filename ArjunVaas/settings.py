"""
Django settings for ArjunVaas project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-q4!q8ouj+*o$gin5unr16bi#d*3+sjv)(!5gmwfc2#+=kj0+zu"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# TODO - LOCAL
# ALLOWED_HOSTS = []

# TODO - PRODUCTION
ALLOWED_HOSTS = [
    "https://ec2-13-234-37-12.ap-south-1.compute.amazonaws.com",
    "ec2-13-234-37-12.ap-south-1.compute.amazonaws.com",
    "13.234.37.12",
    "localhost",
    "127.0.0.1",
    "www.heroheroine.in",
    "ec2-65-2-130-251.ap-south-1.compute.amazonaws.com",
    "http://ec2-65-2-130-251.ap-south-1.compute.amazonaws.com",
    "65.2.130.251",
]
CSRF_TRUSTED_ORIGINS = [
    "https://ec2-13-234-37-12.ap-south-1.compute.amazonaws.com",
    "https://*.ec2-13-234-37-12.ap-south-1.compute.amazonaws.com",
    "https://13.234.37.12",
    "http://13.234.37.12",
    "http://127.0.0.1",
    "http://ec2-65-2-130-251.ap-south-1.compute.amazonaws.com",
    "http://65.2.130.251",
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "ArjunVaas",
    "Accounts",
    "crispy_forms",
    "crispy_bootstrap4",  # TODO - Comment out for production
]

CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ArjunVaas.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ArjunVaas.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

"""
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
"""

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# TODO - LOCAL
# STATIC_URL = 'static/'
# TODO - PRODUCTION
STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = (
    # location of your application, should not be public web accessible
    os.path.join(BASE_DIR, "static"),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
