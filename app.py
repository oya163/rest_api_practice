import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.items import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__)
# If on heroku or environ variable defined, then connect to DATABASE_URL
# else connect to sqlite:///datab.db
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///datab.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key = 'oyesh'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True)
