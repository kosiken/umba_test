from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    DB_URL = 'sqlite:///' + path.join(basedir, 'main', 'database') + environ.get('DB_URL')
    DB_URL_PROD = environ.get('DB_URL_PROD')
    FLASK_ENV = environ.get('FLASK_ENV', 'development')
    REDIS_URL = environ.get("REDIS_CONNECTION_URL")
    CACHE_TYPE = environ.get('CACHE_TYPE')
    CACHE_REDIS_HOST = environ.get('CACHE_REDIS_HOST')
    CACHE_REDIS_PORT = environ.get('CACHE_REDIS_PORT')
    CACHE_REDIS_DB = environ.get('CACHE_REDIS_DB')
    CACHE_REDIS_URL = environ.get('CACHE_REDIS_URL')
    CACHE_DEFAULT_TIMEOUT = environ.get('CACHE_DEFAULT_TIMEOUT')
