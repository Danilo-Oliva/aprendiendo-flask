from flask import (
    request,
    make_response,
    redirect,
    render_template,
    session,
    url_for,
    flash,
)
import unittest
from app import create_app
from app.forms import LoginForm

app = create_app()

items = ["Arroz", "Huevos", "Café", "Leche"]

# creamos un comando propio de flask para ejecutarlo desde consola
@app.cli.command()
def test():
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template("404.html", error=error)


@app.route("/index")
def index():
    user_ip_information = (
        request.remote_addr
    )  # Esto obtiene la dirección IP del cliente

    # La persona que entre al index va a ser automaticamente dirigido hacia la ruta que le digamos al redirect
    response = make_response(redirect(url_for("show_information", _external=True)))
    # con esta response voy a crear una cookie
    # response.set_cookie("user_ip_information", user_ip_information)

    # con esto creamos una sesion donde se va a almacenar los datos y no en una cookie
    session["user_ip_information"] = user_ip_information

    return response


@app.route("/show_information_address")
def show_information():
    user_ip = session.get("user_ip_information")
    username = session.get("username")

    # creo el diccionario que contendrá todos los parametros del render_template
    context = {
        "user_ip": user_ip,
        "items": items,
        "username": username,
    }

    return render_template("ip_information.html", **context)


# punto de entrada
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81, debug=True)
