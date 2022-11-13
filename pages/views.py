from django.shortcuts import render
from .models import SensorFluxo, SensorUmidade
import pandas as pd

def index(request):
    return render(request, "index.html")


def umidade(request):
    sensor = SensorUmidade.objects.all().values()
    df=pd.DataFrame(sensor)
    horario = df['data'].dt.strftime('%d/%m/%Y-%H:%M:%S')
    df1=horario.tolist()
    df=df['dados'].tolist()
    mydict={
        'df':df,
        'df1':df1
    }
    return render(request, "umidade.html", context=mydict)


def fluxo(request):
    sensor = SensorFluxo.objects.all().values()
    df=pd.DataFrame(sensor)
    horario = df['data'].dt.strftime('%d/%m/%Y-%H:%M:%S')
    df1=horario.tolist()#[-2:]
    df=df['dados'].tolist()
    mydict={
        'df':df,
        'df1':df1
    }
    
    return render(request, "fluxo.html", context=mydict)