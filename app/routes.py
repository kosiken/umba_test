from flask import Flask
from app.controllers import UserController, UserApiController

# Setting up routing this way allows for more flexibility
# and allows to an experience similar to express(Node.js) router
# interface
def setup_routing(app: Flask):
    app.add_url_rule('/', view_func=UserController.index_page, methods=['GET'])
    app.add_url_rule('/users', view_func=UserController.fetch_users, methods=['GET'])
    app.add_url_rule('/users/<string:page>',view_func=UserController.fetch_users, methods=['GET'])
    app.add_url_rule('/api/users/profiles', view_func=UserApiController.api_fetch_users, methods=['GET'])
    pass
