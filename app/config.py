from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    DB_URL = 'sqlite:///' + path.join(basedir, 'main', 'database') + environ.get('DB_URL')
    DB_URL_PROD = environ.get('DB_URL_PROD')
    FLASK_ENV = environ.get('FLASK_ENV', 'development')

