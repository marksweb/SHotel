from django.db import models
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField
from backend.apps.utils.choices import SEX_CHOICES


class Employee(AbstractUser):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        null=True,
        blank=True
    )
    birth_date = models.DateField()
    phone_number = PhoneNumberField()
    passport_number = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
