from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'H2OIQ.views.home', name='home'),
    url(r'^/', include('main_app.urls', namespace='main_app')),
    url(r'^admin/', include(admin.site.urls)),
)
