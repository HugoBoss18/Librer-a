# cuentas/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import FormularioCambioUsuario, FormularioCreacionUsuario

UsuarioPersonalizado = get_user_model()


@admin.register(UsuarioPersonalizado)
class UsuarioPersonalizadoAdmin(UserAdmin):
    add_form = FormularioCreacionUsuario
    form = FormularioCambioUsuario
    model = UsuarioPersonalizado
    list_display = ["email", "username", "fecha_nacimiento", "is_superuser"]