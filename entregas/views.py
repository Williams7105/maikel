from django.shortcuts import render
from .models import Entrega

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