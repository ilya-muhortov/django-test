from django.conf.urls import patterns, url

from project.demo.views import DemoUserEditableListView, DemoUserCreateView, RoomEditableListView

urlpatterns = patterns('',
    url(r'^$', 'project.demo.views.home', name='home'),
    url(r'^users/$', DemoUserEditableListView.as_view(), name='user-list'),
    url(r'^rooms/$', RoomEditableListView.as_view(), name='room-list'),
    url(r'^users/create/$', DemoUserCreateView.as_view(), name='user-create'),
)