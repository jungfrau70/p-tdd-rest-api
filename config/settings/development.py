from .base import *


OPTIONAL_APPS = [
    'django_extensions',
]

INSTALLED_APPS = BASE_APPS + OPTIONAL_APPS

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

