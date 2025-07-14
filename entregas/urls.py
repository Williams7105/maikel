from django.urls import path
from .views import vista_mapa, ver_estadisticas
from .views import pagina_inicio


urlpatterns = [
    path("", pagina_inicio, name="inicio"),
    path("mapa-vista/", vista_mapa, name="vista_mapa"),
    path("estadisticas/", ver_estadisticas, name="estadisticas"),
]