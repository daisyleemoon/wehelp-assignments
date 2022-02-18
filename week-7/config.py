from os import path

# from dotenv import load_dotenv

# TESTING = True
# DEBUG = True
# FLASK_ENV = "development"
# SECRET_KEY = "\xf9:\xb7\x7f\xbc\xbcsF1\xec\xa3F"
# DATABASE_URI = 'mysql://root:12345678@localhost:port?pool_name ="mypool"&pool_size=1'


basedir = path.abspath(path.dirname(__file__))
# load_dotenv(path.join(basedir, ".env"))


class Config:
    FLASK_ENV = "development"
    TESTING = True
    SECRET_KEY = "\xf9:\xb7\x7f\xbc\xbcsF1\xec\xa3F"
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    USER = "root"
    PASSWORD = "12345678"
    HOST = "127.0.0.1"
    DATABASE = "website"
