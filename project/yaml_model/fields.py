# coding: utf-8

from django.db import models

# TODO: лучше конечно придумать, что-то типа YAMLDateField, YAMLCharField...


class YAMLField(object):

    def __init__(self, field):
        self.title = field['title']
        self.name = field['id']
        self.type = field['type']

    def get_model_field(self):
        if self.type == 'char':
            return self.char_field()
        elif self.type == 'int':
            return self.int_field()
        elif self.type == 'date':
            return self.date_field()
        else:
            raise Exception('Field type "%s" not found.' % self.type)

    def char_field(self):
        defaults = {
            'max_length': 255,
            'null': True,
            'blank': False,
            'verbose_name': self.title
        }
        return models.CharField(**defaults)

    def int_field(self):
        defaults = {
            'null': True,
            'blank': False,
            'verbose_name': self.title
        }
        return models.IntegerField(**defaults)

    def date_field(self):
        defaults = {
            'null': True,
            'blank': False,
            'verbose_name': self.title
        }
        return models.DateField(**defaults)