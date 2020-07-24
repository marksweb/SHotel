from datetime import datetime, timedelta

from django.contrib.auth import get_user_model

from faker import Faker

from apps.management.models import Room, RoomType
from ...models import Reservation, Guest

User = get_user_model()
fake_profile = Faker().simple_profile()


class TestReservation:

    def setUp(self):
        self.employee, _ = User.objects.get_or_create(
            username=fake_profile['username'],
            first_name='John',
            last_name='Doe',
            sex='M',
            birth_date='1996-01-23',
            phone_number='+48123456789',
            passport_number='AEO123456'
        )

        self.guest = Guest.objects.create(first_name='John',
                                          last_name='Doe',
                                          sex='M',
                                          birth_date='2007-01-01',
                                          nationality='US',
                                          passport_number='AEO123456',
                                          phone_number='+491112345678',
                                          email='john@example.com')
        self.room_type = RoomType.objects.create(name='Premium')
        self.room = Room.objects.create(number=110,
                                        room_type=self.room_type,
                                        price=123.34,
                                        is_for_disabled=False,
                                        is_for_smokers=False,
                                        comment=None)
        self.reservation = Reservation.objects.create(room=self.room,
                                                      guest=self.guest,
                                                      check_in=datetime.today(),
                                                      check_out=datetime.today() + timedelta(days=10),
                                                      made_by=self.employee)

    def test_is_room(self):
        assert isinstance(self.reservation, Reservation)
