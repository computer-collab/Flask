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
class Employees(db.Model):
  __bind_key__ = "employees"
  __tablename__ = "Employees"
  name = db.Column(db.String(200),nullable=False)
  phone_number = db.Column(db.String(10),primary_key=True)
  email_address = db.Column(db.String(2000),nullable=False)
  worker_type = db.Column(db.String(1000),nullable=False)

class WorkingEmployees(Employees):
  __bind_key__ = "employees"
  __tablename__ = "Working_Employees"
  salary = db.Column(db.Integer,nullable = False)