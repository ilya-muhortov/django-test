# coding: utf-8

import datetime

from django.utils import unittest

from project.tests.yaml.models import TestModel


class TestModelTestCase(unittest.TestCase):

    def test_object_create(self):
        TestModel.objects.create(name=u'Илья', paycheck=100, date_joined=datetime.datetime.today())