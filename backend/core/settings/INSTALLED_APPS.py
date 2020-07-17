INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # required apps
    'django_countries',
    'phonenumber_field',
    'rest_framework',

    # project apps
    'apps.reservations',
    'apps.management',

    # dev apps
    'django_extensions',
]
