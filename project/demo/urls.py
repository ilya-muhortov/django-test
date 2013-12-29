from django.conf.urls import patterns, url

from project.demo.views import DemoUserEditableListView

urlpatterns = patterns('',
    url(r'^users/$', DemoUserEditableListView.as_view(), name='user-list'),
)