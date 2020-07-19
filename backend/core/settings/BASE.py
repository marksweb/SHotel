import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = bool(os.environ['DEBUG'])

ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(' ')

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
