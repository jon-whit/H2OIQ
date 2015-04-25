from django.db import models

class WateringStation(models.Model):
    """
    Represents a watering station with a unique station ID.
    """

    # the unique station ID of this station
    station_id = models.BigIntegerField(primary_key=True, unique=True)

    # optional latitudinal and longitudinal coordinates of this station
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    # an optional description
    description = models.TextField(default="")

    def start_watering(self):
        """
        Starts the watering process at this station.
        """
        print ("Starting to water...")

    def stop_watering(self):
        """
        Stops the watering process at this station.
        """
        print ("Stopping the water...")

    def read_moisture(self):
        """
        Reads the moisture value at this station.

        :return:
        """
        print ("Reading soil moisture level...")

    def get_status(self):
        """
        Gets the current status of this station. A station has three operational statuses: watering, idle, and offline.

        :return:
        """
        print ("Getting status...")

    def get_mode(self):
        """
        Gets the current mode of this station. A station has two modes of operation: manual and automatic.

        :return:
        """
        print ("Getting mode...")

    def reset_station(self):
        """
        Resets this station by sending a command to cycle the power.
        """
        print ("Resetting station...")
