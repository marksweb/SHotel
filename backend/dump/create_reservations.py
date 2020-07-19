import random
import string

from django.db import IntegrityError

from apps.reservations.models import Guest
from apps.management.models import Room, Employee

from faker import Faker


fake = Faker()


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_reservations():
    rooms = Room.objects.all()
    employees = Employee.objects.all()

    for _ in range(random.randrange(rooms.count())):
        guest = Guest.objects.create(first_name=fake.first_name(),
                                     last_name=fake.last_name(),
                                     sex=random.choice(['M', 'F']),
                                     birth_date=fake.date(),
                                     birth_place=fake.city(),
                                     nationality=fake.country_code(),
                                     passport_number=id_generator(),
                                     phone_number=fake.phone_number(),
                                     email=fake.email(),
                                     comment=fake.text())
        try:
            guest.reservations.create(room=random.choice([room for room in rooms]),
                                      guest=guest,
                                      check_in=fake.date_between(start_date='today',
                                                                 end_date='+14d'),
                                      check_out=fake.date_between(start_date='today',
                                                                  end_date='+14d'),
                                      made_by=random.choice(employees))
        except IntegrityError:
            continue
