from django.db import models
from django.core.exceptions import ValidationError
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
        max_length=20,
        choices=OPCIONES_ESTADO,
        default="pendiente"
    )
    repartidor = models.ForeignKey(User, on_delete=models.CASCADE)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.codigo} - {self.estado}"

    def clean(self):
        if self.latitud is not None and not (-90 <= self.latitud <= 90):
            raise ValidationError(
                "La latitud debe estar entre -90 y 90 grados."
            )
        if self.longitud is not None and not (-180 <= self.longitud <= 180):
            raise ValidationError(
                "La longitud debe estar entre -180 y 180 grados."
            )