import os

from django.contrib.auth.models import User


def create_admin():
    User.objects.create_superuser(
        username=os.environ['SUPERUSER_USERNAME'],
        password=os.environ['SUPERUSER_PASSWORD']
    )
