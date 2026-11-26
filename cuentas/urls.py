# cuentas/urls.py
from django.urls import path

from .views import VistaCierreSesion, VistaRegistro

urlpatterns = [
    path("logout/", VistaCierreSesion.as_view(), name="logout"),
    path("registro/", VistaRegistro.as_view(), name="registro"),
]