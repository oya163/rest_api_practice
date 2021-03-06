import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.items import Item, ItemList
from resources.store import Store, StoreList

from db import db

app = Flask(__name__)
# If on heroku or environ variable defined, then connect to DATABASE_URL
# else connect to sqlite:///datab.db
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# It helps to propagate the errors generated from
# flask extensions like flask-jwt, flask-jwt-extended
app.config['PROPAGATE_EXCEPTIONS']=True;
app.secret_key = 'oyesh'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
