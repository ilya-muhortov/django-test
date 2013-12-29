# coding: utf-8

from project.yaml_model.models import YAMLModel
from django.db import models


class DemoUser(YAMLModel):

    class Meta:
        db_table = 'demo_users'

    class YAMLMeta:
        schema_name = 'users'

    def __unicode__(self):
        return self.name