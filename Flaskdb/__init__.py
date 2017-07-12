from flask import Flask

app = Flask(__name__)
app.secret_key = 'appsecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///phonebook.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

import Flaskdb.views
