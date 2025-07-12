from rest_framework import viewsets
from .models import Entrega
from .serializers import EntregaSerializer
from django.shortcuts import render


def vista_mapa(request):
    return render(request, "entregas/mapa.html")


class EntregaViewSet(viewsets.ModelViewSet):
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer
