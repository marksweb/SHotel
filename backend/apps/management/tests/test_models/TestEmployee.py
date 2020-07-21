from ...models import Employee


class TestEmployee:

    def setUp(self):
        self.employee = Employee.objects.create(first_name='John',
                                                last_name='Doe',
                                                sex='M',
                                                birth_date='1996-01-23',
                                                function='RT',
                                                phone_number='+48123456789',
                                                passport_number='AEO123456')

    def test_is_employee(self):
        assert isinstance(self.employee, Employee)
