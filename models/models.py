from flask_sqlalchemy import SQLAlchemy
from enum import Enum
from flask import Flask

models = Flask(__name__)
db = SQLAlchemy()


#CREATING THE ENUMS FOR THE EMPLOYEE MODELS
class WorkerType(Enum):
  class SHIRTS(Enum):
    SHIRT_MAKER = "SHIRT_MAKER"

  class PANTS(Enum):
    PANT_MAKER="PANT_MAKER"
  
  UNKNOWN = "UNKNOWN"
    

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

  # PROFILES OF THE WORKERS
class EmployeeProfiles(db.Model):
  __bind_key__ = "employees"
  employee_name = db.Column(db.String(1000),nullable=False)
  employee_id = db.Column(db.String(10),primary_key=True, nullable= False)
  profile_pic = db.Column(db.String(100000), unique=True, nullable= False)
  employee_phoneno = db.Column(db.String())
  employee_type = db.Column(db.Enum(WorkerType),default=WorkerType.UNKNOWN)

class Employees(db.Model):
  __bind_key__ = "employees"
  __tablename__ = "Employees"
  name = db.Column(db.String(200),nullable=False)
  phone_number = db.Column(db.String(10),primary_key=True)
  email_address = db.Column(db.String(2000),nullable=False)
  worker_type = db.Column(db.String(1000),nullable=False)

class WorkingEmployees(Employees):
  pass
#   __bind_key__ = "employees"
#   __tablename__ = "Working_Employees"
#   salary = db.Column(db.Integer,nullable = False)