from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ...utils import SEX_CHOICES


class Employee(models.Model):
    FUNCTION_CHOICES = (
        ('HO', 'Hotel Owner'),
        ('SV', 'Supervisor'),
        ('RT', 'Receptionist'),
        ('RS', 'Room Service'),
        ('CG', 'Concierge'),
        ('BB', 'Bell Boy'),
        ('HK', 'House Keeping'),
        ('CH', 'Chef'),
        ('WT', 'Waiter'),
        ('BT', 'Bartender'),
        ('EG', 'Engineer'),
        ('OT', 'Other'),
    )

    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES,
                           null=True, blank=True)
    birth_date = models.DateField()
    function = models.CharField(max_length=2, choices=FUNCTION_CHOICES)
    phone_number = PhoneNumberField()
    passport_number = models.CharField(max_length=30)
