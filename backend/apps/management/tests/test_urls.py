from django.contrib.auth import get_user_model

from rest_framework.test import APIClient

from faker import Faker

User = get_user_model()
fake_profile = Faker().simple_profile()


class TestUrls:

    def setUp(self):
        self.client = APIClient()
        self.user, _ = User.objects.get_or_create(
            username=fake_profile['username'],
            first_name='John',
            last_name='Doe',
            sex='M',
            birth_date='1996-01-23',
            phone_number='+48123456789',
            passport_number='AEO123456'
        )

    def test_rooms(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/management/rooms/')
        assert response.status_code == 200

        self.client.logout()
        response = self.client.get('/api/management/rooms/')
        assert response.status_code != 200

    def test_roomtypes(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/management/roomtypes/')
        assert response.status_code == 200

        self.client.logout()
        response = self.client.get('/api/management/roomstypes/')
        assert response.status_code != 200

    def test_employees(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/management/employees/')
        assert response.status_code == 200

        self.client.logout()
        response = self.client.get('/api/management/employees/')
        assert response.status_code != 200
