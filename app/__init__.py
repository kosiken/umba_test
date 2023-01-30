
import os
import sys

# this fixes some import errors
sys.path.insert(0, os.getcwd())

from app.server import app, create_table
from app.routes import setup_routing

setup_routing(app)


def run_app():
    port = int(os.environ.get('PORT', 5000))
    create_table()
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    run_app()

