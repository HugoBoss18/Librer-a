from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import FormularioCambioUsuario,FormularioCreacionUsuario

UsuarioPersonalizado = get_user_model()

# Register your models here.
@admin.register(UsuarioPersonalizado)
class UsuarioPersonalizadoAdmin(UserAdmin):
    add_form = FormularioCreacionUsuario
    form = FormularioCambioUsuario
    model = UsuarioPersonalizado
    list_display = ['username', 'email', 'is_superuser']
