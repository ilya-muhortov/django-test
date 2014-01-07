# coding: utf-8

from project.yaml_model.models import YAMLModel
from django.db import models


class TestModel(YAMLModel):

    class Meta:
        pass

    class YAMLMeta:
        schema_name = 'test_model'

    def __unicode__(self):
        return self.name
