import factory
from factory.django import DjangoModelFactory
import json

from django.test import TestCase

from .models import Employee, Department


class DepartmentFactory(DjangoModelFactory):
    FACTORY_FOR = Department

    name = u'HR'


class EmployeeFactory(DjangoModelFactory):
    FACTORY_FOR = Employee

    first_name = u'John'
    last_name = u'Smith'
    department = factory.SubFactory(DepartmentFactory)


class EmployeeTestCase(TestCase):
    def test_users(self):
        EmployeeFactory.create_batch(10)

        res = self.client.get('/api/get_users/')
        self.assertEqual(res.status_code, 200)
        content = json.loads(res.content)

        self.assertIn('status', content)
        self.assertEqual('ok', content['status'])

        self.assertIn('data', content)
        user_data = content['data']
        self.assertEqual(10, len(user_data))

    def test_user(self):
        e = EmployeeFactory()
        res = self.client.get('/api/get_user/', {'id': e.id})

        self.assertEqual(res.status_code, 200)
        content = json.loads(res.content)

        self.assertIn('status', content)
        self.assertEqual('ok', content['status'])

        self.assertIn('data', content)
        user_data = content['data']
        self.assertEqual(user_data['first_name'], u'John')
        self.assertEqual(user_data['last_name'], u'Smith')
