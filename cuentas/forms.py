# cuentas/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class FormularioCreacionUsuario(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username", "fecha_nacimiento")


class FormularioCambioUsuario(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username", "fecha_nacimiento")