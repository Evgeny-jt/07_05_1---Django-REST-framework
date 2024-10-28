from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=100)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensor_id')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
