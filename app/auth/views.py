from . import auth # . es directorio actual
from app.forms import LoginForm
from flask import render_template, flash, session, redirect, url_for

@auth.route("/login", methods=["GET", "POST"])
#acá renderizamos el formulario de login
def login():
  login_form = LoginForm()
  
  context = {
    "login_form":login_form
  }
  
  # validamos
  if login_form.validate_on_submit():
      username = login_form.username.data
      session["username"] = username
      flash("Nombre de usuario registrado correctamente")
      return redirect(url_for("index", _external=True))

  return render_template("login.html", **context)