from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('umidade/', views.umidade, name="umidade"),
    path('fluxo/', views.fluxo, name="fluxo")
]