import os

class Config:
  '''
  General configuration parent class

  '''
  pass

class ProdConfig(Config):
  '''
  Production configuration child class

  Args: 
    Config: The parent configuration class with General configuration settings
  '''
  pass

class DevConfig(Config):
  '''
  Development configuration child class

  Args:
    Config: The parent cinfiguration class with General configuration settings
  '''
  DEBUG = True

config_options = {
  'production': ProdConfig,
  'development': DevConfig
}