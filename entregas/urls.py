from django.urls import path
from .views import pagina_inicio, vista_mapa, ver_estadisticas
from .views import nueva_entrega

urlpatterns = [
    path("", pagina_inicio, name="inicio"),
    path("mapa-vista/", vista_mapa, name="vista_mapa"),
    path("estadisticas/", ver_estadisticas, name="estadisticas"),
    path("entregas/nueva/", nueva_entrega, name="nueva_entrega"),


]