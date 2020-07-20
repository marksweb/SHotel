import sys


TESTING = 'test' in sys.argv

if TESTING:
    PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.MD5PasswordHasher',
    ]

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-erase',
    '--cover-package=apps.reservations,apps.management',
    '--stop',
]
