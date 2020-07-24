from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from apps.utils.choices import SEX_CHOICES


class Guest(models.Model):

    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        null=True,
        blank=True
    )
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=150)
    nationality = CountryField()
    passport_number = models.CharField(max_length=30)
    phone_number = PhoneNumberField()
    email = models.EmailField()
    comment = models.TextField(
        max_length=500,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
