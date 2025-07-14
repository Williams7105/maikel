from django.shortcuts import render
from rest_framework import viewsets
from .models import Entrega
from .serializers import EntregaSerializer

class EntregaViewSet(viewsets.ModelViewSet):
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer

def ver_estadisticas(request):
    pendientes = Entrega.objects.filter(estado="pendiente").count()
    en_ruta = Entrega.objects.filter(estado="en_ruta").count()
    entregadas = Entrega.objects.filter(estado="entregada").count()
    total = Entrega.objects.count()

    context = {
        "pendientes": pendientes,
        "en_ruta": en_ruta,
        "entregadas": entregadas,
        "total": total,
    }
    return render(request, "entregas/estadisticas.html", context)

def vista_mapa(request):
    return render(request, "entregas/mapa.html")