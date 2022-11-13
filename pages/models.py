from django.db import models
from django.utils import timezone


class SensorUmidade(models.Model):
    dados = models.FloatField()
    data = models.DateTimeField(default=timezone.now)

class SensorFluxo(models.Model):
    dados = models.FloatField()
    data = models.DateTimeField(default=timezone.now)