import requests
import json
from celery.schedules import crontab
import os.path
import os
from .common import *

DEBUG = True
ALLOWED_HOSTS = ["*"]
INTERNAL_IPS = [
    # ...
    "172.23.0.1",
    # ...
]


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]


LANGUAGE_CODE = "en-us"
TIME_ZONE = os.environ.get("TZ")
USE_I18N = True
USE_L10N = True
USE_TZ = False


STATIC_URL = "/static/"

STATIC_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../../', 'static'))
