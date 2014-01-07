# coding: utf-8

import json

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic.list import View, MultipleObjectMixin
from django.views.generic.edit import CreateView
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import models as model_forms

from project.demo.models import DemoUser, Room
from project.demo.forms import DemoUserForm


def home(request):
    return render(request, 'demo/home.html')


class EditableListView(MultipleObjectMixin, View):

    def json_response(self, context):
        return HttpResponse(json.dumps(context, cls=DjangoJSONEncoder), content_type='application/json')

    def get(self, request, *args, **kwargs):

        context = {
            'fields': [], 'object_list': []
        }
        opts = self.model._meta
        for field in opts.fields:
            context['fields'].append((field.name, field.verbose_name, field.get_internal_type()))

        for object in self.get_queryset():
            context['object_list'].append([getattr(object, f.name, '') for f in opts.fields])

        return self.json_response(context)

    def post(self, request, *args, **kwargs):
        try:
            pk = int(request.POST.get('object_pk'))
            object = self.get_queryset().get(pk=pk)
        except (ValueError, self.model.DoesNotExist) as e:
            raise Http404

        opts = self.model._meta
        field = request.POST.get('field')
        value = request.POST.get('value')
        if field in [f.name for f in opts.fields]:
            form_class = model_forms.modelform_factory(self.model, fields=[field])
            form = form_class({field: value}, instance=object)
            if form.is_valid():
                object = form.save()

                return self.json_response({'value': getattr(object, field, '')})
            else:
                return self.json_response({'error': form[field].errors.as_text(), 'value': value})

        return self.json_response({'error': u'Field %s does not exist.' % field, 'value': value})



class DemoUserEditableListView(EditableListView):

    model = DemoUser
    form_class = DemoUserForm
    template_name = 'demo/user_list.html'


class RoomEditableListView(EditableListView):

    model = Room


class DemoUserCreateView(CreateView):

    model = DemoUser
    template_name = 'demo/user_create.html'
    success_url = 'demo:user-list'