from django.contrib.auth import get_user_model  # type: ignore[reportMissingModuleSource]
from django.contrib.auth.forms import UserCreationForm, UserChangeForm  # type: ignore[reportMissingModuleSource]

class FormularioCreacionUsuario(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')

class FormularioCambioUsuario(UserChangeForm):
    class Meta:
        model=get_user_model()
        fields = ('username', 'email')

