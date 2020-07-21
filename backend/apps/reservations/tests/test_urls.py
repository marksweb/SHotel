from django.contrib.auth.models import User

from rest_framework.test import APIClient


class TestUrls:

    def setUp(self):
        self.client = APIClient()
        self.user, _ = User.objects.get_or_create(username='sonofthebitch',
                                                  password='somepassword123',
                                                  email='john@example.com')

    def test_guests(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/reservations/guests/')
        assert response.status_code == 200

        self.client.logout()
        response = self.client.get('/api/reservations/guests/')
        assert response.status_code != 200

    def test_reservations(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/reservations/reservations/')
        assert response.status_code == 200

        self.client.logout()
        response = self.client.get('/api/reservations/reservations/')
        assert response.status_code != 200
