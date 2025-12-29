from . import auth # . es directorio actual
from app.forms import LoginForm

@auth.route("/login")
#acá renderizamos el formulario de login
def login():
  context = {
    "login_form":LoginForm()
  }
  return ""