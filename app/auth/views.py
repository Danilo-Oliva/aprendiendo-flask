from . import auth # . es directorio actual
from app.forms import LoginForm
from flask import render_template

@auth.route("/login")
#acá renderizamos el formulario de login
def login():
  context = {
    "login_form":LoginForm()
  }
  return render_template("login.html", **context)