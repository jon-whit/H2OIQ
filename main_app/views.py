import datetime

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the H20IQ index.")


def schedule(request):
    return HttpResponse("Hello, world. You're at the H20IQ schedule.")


def monitor(request):
    return HttpResponse("Hello, world. You're at the H20IQ monitor.")


def stations(request):
    # for ws in WateringStation.objects.all():
    # do something...
    return HttpResponse("Hello, world. You're at the H20IQ stations.")


def settings(request):
    return HttpResponse("Hello, world. You're at the H20IQ settings.")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
