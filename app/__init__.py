#Este archivo se va a encargar de crear la app
from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config

def create_app():
  app = Flask(__name__)
  bootstrap = Bootstrap(app)
  app.config.from_object(Config)#Va a tomar la configuracion que viene desde Config
  
  return app