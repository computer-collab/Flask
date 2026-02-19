from flask_sqlalchemy import SQLAlchemy
from flask import Flask

models = Flask(__name__)
db = SQLAlchemy()


class register(db.Model):
  __bind_key__ = "dbadmin"
  name = db.Column(db.String(256),nullable = False)
  username = db.Column(db.String(256),primary_key=True)
  password = db.Column(db.String(1000),nullable=False)
  email = db.Column(db.String(256),nullable=False)
  token = db.Column(db.String(256))

class RegisteringAdmins(db.Model):
  __bind_key__ = "dbadmin"
  name = db.Column(db.String(256),nullable = False)
  username = db.Column(db.String(256),primary_key=True)
  password = db.Column(db.String(1000),nullable=False)
  email = db.Column(db.String(256),nullable=False)
  token = db.Column(db.String(256))
