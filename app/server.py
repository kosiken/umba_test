import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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

db.init_app(app)

def create_table():
    with app.app_context():
        db.metadata.create_all(bind=db.engine, checkfirst=True)

