# coding: utf-8

from django.contrib import admin

from project.demo.models import DemoUser


class DemoUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(DemoUser, DemoUserAdmin)
