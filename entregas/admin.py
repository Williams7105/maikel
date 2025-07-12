from django.contrib import admin
from django.utils.html import format_html
from .models import Entrega


@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    list_display = ("codigo", "direccion", "estado_coloreado", "repartidor", "creado")
    search_fields = ("codigo", "direccion")
    list_filter = ("estado", "creado")
    date_hierarchy = "creado"
    actions = ["marcar_entregado"]

    def estado_coloreado(self, obj):
        colores = {"pendiente": "orange", "en camino": "blue", "entregado": "green"}
        color = colores.get(obj.estado, "gray")
        return format_html(
            f"<span style='color:{color}; font-weight:bold;'>{obj.estado.upper()}</span>"
        )

    estado_coloreado.short_description = "Estado"

    def marcar_entregado(self, request, queryset):
        actualizadas = queryset.update(estado="entregado")
        self.message_user(
            request, f"{actualizadas} entrega(s) marcadas como entregadas."
        )
