from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^schedule/', views.schedule, name='schedule'),
    url(r'^monitor/', views.monitor, name='monitor'),
    url(r'^stations/', views.stations, name='stations'),
    url(r'^settings/', views.settings, name='settings'),
]
