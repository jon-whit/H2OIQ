from django.db import models

class WateringStation(models.Model):
    """
    Represents a watering station with a unique station ID.
    """

    station_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=200)
