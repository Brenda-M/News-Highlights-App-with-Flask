from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

def create_app(config_name):
  
  app = Flask(__name__)

  #Create the app configurations
  app.config.from_object(config_options[config_name])

  #Intialize flask extensions
  bootstrap.init_app(app)

  from 

  return app