from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from entregas.views import EntregaViewSet

router = routers.DefaultRouter()
router.register(r"entregas", EntregaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),  # Para API REST
    path("", include("entregas.urls")),  # Para vistas como /mapa-vista/
]
