# coding: utf-8

from project.yaml_model.models import YAMLModel
from django.db import models


class DemoUser(YAMLModel):

    class Meta:
        pass

    class YAMLMeta:
        schema_name = 'users'

    def __unicode__(self):
        return self.name


class Room(YAMLModel):

    class Meta:
        pass

    class YAMLMeta:
        schema_name = 'rooms'

    def __unicode__(self):
        return u'%s (%d)' % (self.department, self.spots)