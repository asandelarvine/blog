import os 

class Config:
  SECRET_KEY = "1234"
  SQLALCHEMY_DATABASE_URI = 'postgresql://yglntfnbuxylas:ac70f8c58fe2a0c44d65582347759781e73c407d8b560170ccdc204f5af8cafd@ec2-52-201-195-11.compute-1.amazonaws.com:5432/d7km0aikrrd2ja'
  UPLOADED_PHOTOS_DEST = "app/static/photos"

  # email configurations
  MAIL_SERVER = "smtp.gmail.com"
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = "monkeymee20you@gmail.com"
  MAIL_PASSWORD = "@monkey2000"

class ProdConfig(Config):
    
  SQLALCHEMY_DATABASE_URI = 'postgresql://yglntfnbuxylas:ac70f8c58fe2a0c44d65582347759781e73c407d8b560170ccdc204f5af8cafd@ec2-52-201-195-11.compute-1.amazonaws.com:5432/d7km0aikrrd2ja'

class TestConfig(Config):
    
  SQLALCHEMY_DATABASE_URI = 'postgresql://yglntfnbuxylas:ac70f8c58fe2a0c44d65582347759781e73c407d8b560170ccdc204f5af8cafd@ec2-52-201-195-11.compute-1.amazonaws.com:5432/d7km0aikrrd2ja'

class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql://yglntfnbuxylas:ac70f8c58fe2a0c44d65582347759781e73c407d8b560170ccdc204f5af8cafd@ec2-52-201-195-11.compute-1.amazonaws.com:5432/d7km0aikrrd2ja'
  DEBUG = True

config_options = {
  "development": DevConfig,
  "production": ProdConfig,
  "test": TestConfig
}