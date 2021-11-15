import os 

class Config:
  SECRET_KEY = "1234"
  SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://access:yooh@localhost/blog"
  UPLOADED_PHOTOS_DEST = "app/static/photos"

  # email configurations
  MAIL_SERVER = "smtp.gmail.com"
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = "monkeymee20you@gmail.com"
  MAIL_PASSWORD = "@monkey2000"

class ProdConfig(Config):
    
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    
  SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://access:yooh@localhost/blog_test"

class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://access:yooh@localhost/blog"
  DEBUG = True

config_options = {
  "development": DevConfig,
  "production": ProdConfig,
  "test": TestConfig
}