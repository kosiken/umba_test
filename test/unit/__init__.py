import pytest
from app.server import app, db, create_table
from app.routes import setup_routing
from flask_sqlalchemy import SQLAlchemy
from scripts.seed import get_users
from app.models import User

def seed_users(app_db: SQLAlchemy):

    with app.app_context():
        prev = app_db.session.execute(
            app_db.select(User).limit(1)
        )
        first = prev.scalar()
        if first is not None:
            return
        users = get_users(15)
        users_to_add = [User(**row) for row in users]
        app_db.session.add_all(users_to_add)
        app_db.session.commit()


@pytest.fixture
def client():
    """Configures the app for testing

    Sets app config variable ``TESTING`` to ``True``

    :return: App for testing
    """
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite://'
    app.config['TESTING'] = True
    try:
        setup_routing(app)
        db.init_app(app)
    except Exception:
        pass
    create_table(db)
    seed_users(db)
    app_client = app.test_client()

    return app_client


