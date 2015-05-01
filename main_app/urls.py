from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^schedule$', views.schedule, name='schedule'),
    url(r'^monitor$', views.monitor, name='monitor'),
    url(r'^monitor/(?P<station_id>[1-9]+[0-9]*)$', views.station_detail, name='monitor_detail'),
    url(r'^stations/$', views.StationsListView.as_view(), name='stations'),
    url(r'^stations/(?P<station_id>[1-9]+[0-9]*)$', views.station_detail, name='station_detail'),
    url(r'^settings$', views.settings, name='settings'),
    url(r'^stations/start/(?P<station_id>[1-9]+[0-9]*)$', views.start_station, name='start_station'),
    url(r'^stations/stop/(?P<station_id>[1-9]+[0-9]*)$', views.stop_station, name='stop_station')
]
