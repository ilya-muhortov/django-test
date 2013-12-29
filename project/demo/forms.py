# coding: utf-8

from django import forms

from project.demo.models import DemoUser


class DemoUserForm(forms.ModelForm):

    class Meta:
        model = DemoUser