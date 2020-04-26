from flask import Flask
from config import config_options

def create_app(config_name):
  
  app = Flask(__name__)

  #Create the app configurations
  app.config.from_object(config_options[config_name])

  #Intialize flask extensions

  return app