# coding: utf-8

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import ModelFormMixin

from project.demo.models import DemoUser
from project.demo.forms import DemoUserForm


class EditableListView(ListView):#, ModelFormMixin):

    pass


class DemoUserEditableListView(EditableListView):

    model = DemoUser
    form_class = DemoUserForm
    template_name = 'demo/user_list.html'