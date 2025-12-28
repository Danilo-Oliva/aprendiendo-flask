from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest

app = Flask(__name__)
bootstap = Bootstrap(app)
app.config["SECRET_KEY"] = 'CLAVE SEGURA'

items = ["Arroz", "Huevos", "Café", "Leche"]

#creamos un comando propio de flask para ejecutarlo desde consola
@app.cli.command()
def test():
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)

class LoginForm(FlaskForm):
    username = StringField("Nombre del usuario", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Enviar datos", validators=[DataRequired()])

@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template('404.html', error = error)


@app.route("/index")
def index():
    user_ip_information = request.remote_addr

    # La persona que entre al index va a ser automaticamente dirigido hacia la ruta que le digamos al redirect
    response = make_response(redirect("/show_information_address"))
    # con esta response voy a crear una cookie
    #response.set_cookie("user_ip_information", user_ip_information)

    #con esto creamos una sesion donde se va a almacenar los datos y no en una cookie
    session["user_ip_information"] = user_ip_information
    
    return response


@app.route("/show_information_address", methods=["GET", "POST"])
def show_information():
    user_ip = session.get("user_ip_information")
    username = session.get("username")
    login_form = LoginForm()
    # creo el diccionario que contendrá todos los parametros del render_template
    context = {"user_ip": user_ip,
               "items": items,
               "login_form": login_form,
               "username": username
               }
    
    #validamos
    if login_form.validate_on_submit():
        username = login_form.username.data
        session["username"] = username
        flash("Nombre de usuario registrado correctamente")
        return redirect(url_for('index'))
        
    return render_template("ip_information.html", **context)

#punto de entrada
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81, debug=True)
