# coding: utf-8

from django.contrib import admin

from project.demo.models import DemoUser, Room


class DemoUserAdmin(admin.ModelAdmin):
    pass


class RoomAdmin(admin.ModelAdmin):
    pass


admin.site.register(DemoUser, DemoUserAdmin)
admin.site.register(Room, RoomAdmin)