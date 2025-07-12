from django.db import models
from django.contrib.auth.models import User

OPCIONES_ESTADO = (
    ("pendiente", "Pendiente"),
    ("en_ruta", "En ruta"),
    ("entregada", "Entregada"),
    ("cancelada", "Cancelada"),
)


class Entrega(models.Model):
    codigo = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    estado = models.CharField(
        max_length=20, choices=OPCIONES_ESTADO, default="pendiente"
    )
    repartidor = models.ForeignKey(User, on_delete=models.CASCADE)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.codigo} - {self.estado}"
