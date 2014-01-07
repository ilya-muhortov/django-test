from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^demo/', include('project.demo.urls', namespace='demo')),
)

if settings.DEBUG is True:
    pass
    #from django.conf.urls.static import static
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)