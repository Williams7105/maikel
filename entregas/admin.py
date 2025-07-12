from django.contrib import admin
from .models import Entrega


@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    list_display = ("codigo", "direccion", "estado", "repartidor", "creado")
    search_fields = ("codigo", "direccion")
    list_filter = ("estado", "creado")
