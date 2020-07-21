from ...models import Guest


class TestGuest:

    def setUp(self):
        self.guest = Guest.objects.create(first_name='John', 
                                          last_name='Doe',
                                          sex='M',
                                          birth_date='2007-01-01',
                                          nationality='US',
                                          passport_number='AEO123456',
                                          phone_number='+491112345678',
                                          email='john@example.com')

    def test_is_room(self):
        assert isinstance(self.guest, Guest)
