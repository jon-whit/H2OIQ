import datetime

from django.http import HttpResponse
from django.views import generic

from main_app.models import WateringStation


def index(request):
    return HttpResponse("Hello, world. You're at the H20IQ index.")


def schedule(request):
    return HttpResponse("Hello, world. You're at the H20IQ schedule.")


def monitor(request):
    return HttpResponse("Hello, world. You're at the H20IQ monitor.")


class StationsListView(generic.ListView):
    template_name = "main_app/stations.html"

    def get_queryset(self):
        return WateringStation.objects.all()


# Old Code, I'm using the generic ListView up above, so if we
# end up not using this, delete it
'''
def stations(request):
    watering_stations = WateringStation.objects.all()
    template = loader.get_template("main_app/stations.html")
    context = RequestContext(request, {"watering_stations": watering_stations, })
    return HttpResponse(template.render(context))
'''


def station_detail(request, station_id):
    return HttpResponse("Hello, world. You're at the H20IQ station_detail.")


def settings(request):
    return HttpResponse("Hello, world. You're at the H20IQ settings.")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
