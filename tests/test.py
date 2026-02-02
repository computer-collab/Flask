from flask import Flask, session, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

test = Flask(__name__)
test.config['SQLALCHEMY_DATABASE_URI']="sqlite:///trail.db"
test.config['SQLALCHEMY_BINDS']={
    'dbadmin' = 'sqlite:///dbadmin.db'
}
db = SQLAlchemy(test)

class register(db.Model):
    username = db.Column(db.String(1000),primary_key=True)
    password = db.Column(db.String(1000),nullable=False)

@test.route('/', methods=['POST','GET'])
def rendertemplate():
    if request.method == 'GET':
        return render_template('x.html')
    if request.method == 'POST':
        