from flask_sqlalchemy import SQLAlchemy
from flask import Flask,session
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///admin.db';
db = SQLAlchemy(app)

class admin(db.Model):
    __tablename__ = "Admin"
    username = db.Column(db.String(100), nullable=False,primary_key=True)
    password = db.Column(db.String(100),nullable=False)


with app.app_context():
    db.create_all()

    db.session.add()
    db.session.commit()