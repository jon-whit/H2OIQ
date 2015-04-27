from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^schedule/', views.schedule, name='schedule'),
    url(r'^monitor/$', views.monitor, name='monitor'),
    url(r'^monitor/(?P<station_id>[0-9]+)/$', views.station_detail, name='monitor_detail'),
    # I was testing out the default templates so commented out the old url
    # url(r'^stations/$', views.stations, name='stations'),
    url(r'^stations/$', views.StationsListView.as_view(), name='stations'),
    url(r'^stations/(?P<station_id>[0-9]+)/$', views.station_detail, name='station_detail'),
    url(r'^settings/', views.settings, name='settings'),
]
