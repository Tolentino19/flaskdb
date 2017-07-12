from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Flaskdb import app

db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    phone = db.Column(db.String(120), unique=True)

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return '<Person %r>' % self.name
