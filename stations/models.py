from django.db import models

class WaterStation(models.Model):
    """
    Represents a watering station with a unique station ID.
    """

    station_id = models.IntegerField()
    description = models.CharField(max_length=200)

    def __str__(self):
        s = "%d\n%s" % (station_id, description)
        return s
