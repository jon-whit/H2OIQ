from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'H2OIQ.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^stations/', include('stations.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
