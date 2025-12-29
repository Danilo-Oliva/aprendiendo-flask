#Este archivo se va a encargar de crear la app
from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from app.auth import auth

def create_app():
  app = Flask(__name__)
  bootstrap = Bootstrap(app)
  app.config.from_object(Config)#Va a tomar la configuracion que viene desde Config
  app.register_blueprint(auth)
  return app