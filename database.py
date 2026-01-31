from flask_sqlalchemy import SQLAlchemy
from flask import Flask,session
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///admin.db';
db = SQLAlchemy(app)

class adminadd(db.Model):
    __tablename__ = "Admin"
    username = db.Column(db.String(100), nullable=False,primary_key=True,unique=True)
    password = db.Column(db.String(100),nullable=False)

NewAdmin = adminadd(
    username = "arun_tailors",
    password = generate_password_hash("12345678")
)

NewAdmin1 = adminadd(
    username = "aruntailors",
    password = generate_password_hash("12345678")
)
with app.app_context():
    db.create_all()

    db.session.add(NewAdmin)
    db.session.add(NewAdmin1)
    db.session.commit()