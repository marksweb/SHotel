import os

from django.contrib.auth import get_user_model

User = get_user_model()


def create_admin():
    User.objects.create_superuser(
        username=os.environ['SUPERUSER_USERNAME'],
        password=os.environ['SUPERUSER_PASSWORD'],
        birth_date='2000-01-01',
        first_name='Super',
        last_name='User'
    )
