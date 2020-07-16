import random
import string

from apps.management.models import Employee

from faker import Faker


fake = Faker()


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_employees():
    # create hotel owner
    Employee.objects.create(first_name=fake.first_name(),
                            last_name=fake.last_name(),
                            sex=random.choice(['M', 'F']),
                            birth_date=fake.date(),
                            function='HO',
                            phone_number=fake.phone_number(),
                            passport_number=id_generator())
    for _ in range(5):
        Employee.objects.create(first_name=fake.first_name(),
                                last_name=fake.last_name(),
                                sex=random.choice(['M', 'F']),
                                birth_date=fake.date(),
                                function='RT',
                                phone_number=fake.phone_number(),
                                passport_number=id_generator())
