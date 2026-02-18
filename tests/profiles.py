from flask import render_template,Flask 
from paths import CURRENT_DIR
from flask_sqlalchemy import SQLAlchemy
from database import User, db
# from database import User

app=Flask(__name__)
# db=SQLAlchemy(app)



def profiles(username):
  # id = username
  # username = None
  print(CURRENT_DIR)
  user = User.query.filter_by(username=username).first()
  print(id)
  if not user:
    return f"<h1>User not found   {username} {id} <h1>"
  return render_template("profiles.html",username=user.username,age=user.age,name=user.name)