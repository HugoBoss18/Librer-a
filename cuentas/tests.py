# cuentas/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse  # nuevo

from .forms import FormularioCreacionUsuario  # nuevo
from .views import VistaRegistro  # nuevo


class PruebasRegistro(TestCase):  # nuevo
    def setUp(self):
        url = reverse("registro")
        self.respuesta = self.client.get(url)

    def test_plantilla_registro(self):
        self.assertEqual(self.respuesta.status_code, 200)
        self.assertTemplateUsed(self.respuesta, "registration/registro.html")
        self.assertContains(self.respuesta, "Registrarse")
        self.assertNotContains(self.respuesta, "Hola, ¿estás perdido?")

    def test_formulario_registro(self):
        formulario = self.respuesta.context.get("form")
        self.assertIsInstance(formulario, FormularioCreacionUsuario)
        self.assertContains(self.respuesta, "csrfmiddlewaretoken")

    def test_url_resuelve_vista_registro(self):
        vista = resolve("/cuentas/registro/")
        self.assertEqual(vista.func.view_class, VistaRegistro)

    def test_registro_crea_usuario(self):
        respuesta = self.client.post(
            reverse("registro"),
            {
                "username": "lectora",
                "email": "lectora@ejemplo.mx",
                "password1": "Clave-segura-2026",
                "password2": "Clave-segura-2026",
            },
        )
        self.assertRedirects(respuesta, reverse("login"))
        usuario = get_user_model().objects.get(username="lectora")
        self.assertEqual(usuario.email, "lectora@ejemplo.mx")


class PruebasSesion(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.usuario = get_user_model().objects.create_user(
            username="usuario",
            password="Clave-segura-2026",
        )

    def test_plantilla_inicio_sesion(self):
        respuesta = self.client.get(reverse("login"))
        self.assertTemplateUsed(respuesta, "registration/login.html")

    def test_inicio_sesion_redirige_a_inicio(self):
        respuesta = self.client.post(
            reverse("login"),
            {"username": "usuario", "password": "Clave-segura-2026"},
        )
        self.assertRedirects(respuesta, reverse("inicio"))

    def test_cierre_sesion_requiere_post_y_redirige_a_inicio(self):
        respuesta_get = self.client.get(reverse("logout"))
        self.assertEqual(respuesta_get.status_code, 405)

        respuesta_post = self.client.post(reverse("logout"))
        self.assertRedirects(respuesta_post, reverse("inicio"))

    def test_inicio_saluda_a_usuario_autenticado(self):
        self.client.force_login(self.usuario)
        respuesta = self.client.get(reverse("inicio"))
        self.assertContains(respuesta, "Hola")

    def test_inicio_no_saluda_a_usuario_anonimo(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertNotContains(respuesta, "Hola")


class PruebasUsuarioPersonalizado(TestCase):
    def test_crear_usuario(self):
        Usuario = get_user_model()
        usuario = Usuario.objects.create_user(
            username="ana",
            email="ana@ejemplo.mx",
            password="Clave-segura-2026",
        )
        self.assertEqual(usuario.username, "ana")
        self.assertEqual(usuario.email, "ana@ejemplo.mx")
        self.assertIsNone(usuario.fecha_nacimiento)
        self.assertTrue(usuario.is_active)
        self.assertFalse(usuario.is_staff)
        self.assertFalse(usuario.is_superuser)

    def test_crear_superusuario(self):
        Usuario = get_user_model()
        admin = Usuario.objects.create_superuser(
            username="jefa",
            email="jefa@ejemplo.mx",
            password="Clave-segura-2026",
        )
        self.assertEqual(admin.username, "jefa")
        self.assertEqual(admin.email, "jefa@ejemplo.mx")
        self.assertTrue(admin.is_active)
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)