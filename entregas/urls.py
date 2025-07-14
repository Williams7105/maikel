from django.urls import path
from .views import vista_mapa

urlpatterns = [
    path("mapa-vista/", vista_mapa, name="vista_mapa"),
]

from .views import ver_estadisticas

urlpatterns += [
    path("estadisticas/", ver_estadisticas, name="estadisticas"),
]