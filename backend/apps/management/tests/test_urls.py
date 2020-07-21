from django.contrib.auth.models import User

from rest_framework.test import APIClient


class TestUrls:

    def setUp(self):
        self.client = APIClient()
        self.user, _ = User.objects.get_or_create(username='sonofthebitch',
                                                  password='somepassword123',
                                                  email='john@example.com')

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
