import os
from flask import Flask
from flask_caching import Cache
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import jinja_partials
from .config import Config


# hopefully the root directory is the cwd

template_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(template_dir, 'views')
# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__, template_folder=template_dir)

if Config.FLASK_ENV == 'production':
    app.config["SQLALCHEMY_DATABASE_URI"] = Config.DB_URL_PROD
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = Config.DB_URL

app.config['CACHE_TYPE'] = Config.CACHE_TYPE
app.config['CACHE_REDIS_HOST'] = Config.CACHE_REDIS_HOST
app.config['CACHE_REDIS_PORT'] = int(Config.CACHE_REDIS_PORT)
app.config['CACHE_REDIS_DB'] = Config.CACHE_REDIS_DB
app.config['CACHE_REDIS_URL'] = Config.CACHE_REDIS_URL
app.config['CACHE_DEFAULT_TIMEOUT'] = Config.CACHE_DEFAULT_TIMEOUT

cache = Cache(app)
migrate = Migrate(app, db)
db.init_app(app)
jinja_partials.register_extensions(app)


@app.cli.command("test")
def app_test():
    print('No tests')


def create_table():
    with app.app_context():
        db.metadata.create_all(bind=db.engine, checkfirst=True)
