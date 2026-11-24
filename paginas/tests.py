# paginas/tests.py
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import VistaInicio  # nuevo


class PruebasPaginaInicio(SimpleTestCase):
    def test_url_existe_en_ubicacion_correcta(self):
        respuesta = self.client.get("/")
        self.assertEqual(respuesta.status_code, 200)

    def test_nombre_url_pagina_inicio(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertEqual(respuesta.status_code, 200)

    def test_plantilla_pagina_inicio(self):  # nuevo
        respuesta = self.client.get("/")
        self.assertTemplateUsed(respuesta, "inicio.html")
        self.assertTemplateUsed(respuesta, "_base.html")

    def test_contenido_pagina_inicio(self):  # nuevo
        respuesta = self.client.get("/")
        self.assertContains(respuesta, "Página de inicio")

    def test_contenido_incorrecto_pagina_inicio(self):  # nuevo
        respuesta = self.client.get("/")
        self.assertNotContains(respuesta, "Hola, ¿estás perdido?")

    def test_html_pagina_inicio(self):  # nuevo
        respuesta = self.client.get("/")
        self.assertContains(respuesta, "<h1>Página de inicio</h1>", html=True, count=1)
        self.assertContains(respuesta, "<title>Librería - Inicio</title>", html=True)

    def test_url_resuelve_vista_inicio(self):  # nuevo
        vista = resolve("/")
        self.assertEqual(vista.func.view_class, VistaInicio)
        self.assertEqual(vista.url_name, "inicio")