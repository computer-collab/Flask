from flask import *
# from database import User
from profiles import profiles
from models import *
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///example.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
with app.app_context():
  db.create_all()
@app.route("/<chitti>")
def view(chitti):
  print(chitti)
  return profiles(chitti)
  
if __name__== "__main__":
  app.run(debug=True)