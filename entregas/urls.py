from django.urls import path
from .views import vista_mapa, ver_estadisticas

urlpatterns = [
    path("mapa-vista/", vista_mapa, name="vista_mapa"),
    path("estadisticas/", ver_estadisticas, name="estadisticas"),
]