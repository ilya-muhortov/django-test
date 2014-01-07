# coding: utf-8

import datetime
import json

from django.test import Client, TestCase

from project.demo.models import DemoUser


class TestDemoUserTestCase(TestCase):

    def setUp(self):
        self.user_1 = DemoUser.objects.create(name='John', paycheck=100, date_joined=datetime.datetime.today())

    def test_demo_user_view(self):
        c = Client()
        response = c.get('/demo/users/')
        self.assertEquals(response.status_code, 200)
        json.loads(response.content)

        params = {'value': 'Sam', 'field': 'name', 'object_pk': self.user_1.pk}
        response = c.post('/demo/users/', params)
        self.user_1 = DemoUser.objects.get(pk=self.user_1.pk)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.user_1.name, 'Sam')

        params = {'value': 'Sam', 'field': 'name_fake', 'object_pk': self.user_1.pk}
        response = c.post('/demo/users/', params)
        self.assertEquals(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('error', data)

        params = {'value': 'Sam', 'field': 'name_fake', 'object_pk': 'fake'}
        response = c.post('/demo/users/', params)
        self.assertEquals(response.status_code, 404)