from django.contrib.auth import get_user_model

from faker import Faker

User = get_user_model()
fake_profile = Faker().simple_profile()


class TestEmployee:

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

    def test_is_employee(self):
        assert isinstance(self.employee, User)
