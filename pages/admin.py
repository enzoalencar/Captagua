from django.contrib import admin
from .models import SensorUmidade, SensorFluxo

class SensorView(admin.ModelAdmin):
    list_display = ('id', 'dados', 'data')

admin.site.register(SensorUmidade, SensorView)
admin.site.register(SensorFluxo, SensorView)