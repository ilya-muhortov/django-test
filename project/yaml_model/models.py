# coding: utf-8

from os import path
import sys
import yaml

from django.db import models
from django.db.models.base import ModelBase
from django.utils import six

from project.yaml_model.fields import YAMLField


class YAMLModelBase(ModelBase):

    def __new__(cls, name, bases, attrs):
        super_new = super(YAMLModelBase, cls).__new__

        if name == 'NewBase' and attrs == {}:
            return super_new(cls, name, bases, attrs)

        new_class = super_new(cls, name, bases, attrs)
        yaml_meta = attrs.pop('YAMLMeta', None)
        if yaml_meta:
            new_class = new_class.create_fields(new_class, yaml_meta)

        return new_class

    @staticmethod
    def create_fields(cls, meta):
        module_dir = path.dirname(path.realpath(sys.modules[cls.__module__].__file__))
        try:
            stream = file('%s/models.yaml' % module_dir, 'r')
            yaml_data = yaml.load(stream)
        except (IOError, yaml.YAMLError) as e:
            raise e

        schema_name = getattr(meta, 'schema_name', None)
        if schema_name and schema_name in yaml_data:
            fields = yaml_data[schema_name]
            for field in fields['fields']:
                yaml_field = YAMLField(field)
                try:
                    cls._meta.get_field(yaml_field.name)
                except models.FieldDoesNotExist:
                    model_field = yaml_field.get_model_field()
                    model_field.contribute_to_class(cls, yaml_field.name)

        return cls


class YAMLModel(six.with_metaclass(YAMLModelBase, models.Model)):

    class Meta:
        abstract = True