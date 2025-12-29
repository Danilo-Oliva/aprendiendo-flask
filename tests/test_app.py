from flask_testing import TestCase
from flask import current_app, url_for
from main import app


class MainTest(TestCase):
    # crea la app dentro del env de testing, con ciertas configuraciones
    def create_app(self):
        # Cuando corre el test, cambia el entorno de desarrollo a testing
        app.config["TESTING"] = True
        # cuando corre el test, deshabilita los tokens que contienen la info
        app.config["WTF_CSRF_ENABLED"] = False
        return app

    # prueba de que la app existe
    def test_app_exists_web(self):
        # verifica que un objeto no sea de tipo none
        self.assertIsNotNone(
            current_app
        )  # se refiere a la app creada dentro del env de testing

    # Verifica de que la app está en el env de prueba
    def test_app_in_testing_mode(self):
        self.assertTrue(current_app.config["TESTING"])

    # Prueba los redirects
    def test_index_redirects(self):
        response = self.client.get(
            url_for("index")
        )  # ´Primero hacemos una petición al index
        # comprobamos que de verdad se hizo el redireccionamiento
        self.assertRedirects(response, url_for("show_information", _external=True))
    
    #Testea la funcion show_information para chequear que el get funcione correctamente, por eso nos devolvera el código 200
    def test_show_information_get(self):
        response = self.client.get(url_for("show_information"))
        self.assert200(response)
    
    #testeamos el post, pero el post devuelve datos, por eso agregamos data    
    def test_show_information_post(self):
        """

        """
        response = self.client.post(url_for("show_information"))
        self.assert405(response, url_for("index", _external=True))#405 significa si fue autorizado
        
    #testeamos de que el blueprint existe
    def test_auth_blueprin_exists_module(self):
        self.assertIn("auth", self.app.blueprints)
    
    #testeamos la ruta del blueprint
    def test_auth_blueprint_get(self):
        response = self.client.get(url_for("auth.login")) #esto porque nos referimos a la funcion de un blueprint
        self.assert200(response)
    
    #testeamos si el blueprint del login está siendo renderizado
    def test_auth_blueprint_login_template(self):
        self.client.get(url_for("auth.login"))
        self.assertTemplateUsed("login.html")
    
    #testeamos el metodo post de la ruta del blueprint del login
    def test_auth_blueprint_login_post(self):
        test_form_fake = {
            "username": "Danilo",
            "password": "123456",
        }
        response = self.client.post(url_for("auth.login"), data=test_form_fake)
        self.assertRedirects(response, url_for("index"))
