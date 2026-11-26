from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class UsuarioPersonalizado(AbstractUser):
    fecha_nacimiento = models.DateField(null=True, blank=True)