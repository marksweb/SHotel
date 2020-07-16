from django.contrib.auth.models import User


def create_admin():
    # TODO: set superuser credentials as env variable
    User.objects.create_superuser(username='admin',
                                  password='seweryn')
