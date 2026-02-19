from flask import Flask, jsonify, request, session, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from modules.mails import GenerateOTP
from modules import *




app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users/data.db'
db = SQLAlchemy(app)
app.secret_key = "this is ultra long secret code"

# =-------- DATABASES ------------------------

#__________USERS SIGNUP _______________________

class SignedUsers(db.Model):
    Email = db.Column(db.String(1000),nullable = False, primary_key=True)
    Password = db.Column(db.String(1000), primary_key=False, nullable=False)


#--------- CREATING THE DATA BASE -----------
with app.app_context():
    db.create_all()
    


#----------- ROUTES --------------


# ___________404 not found ____________
@app.errorhandler(404)
def errorhanler(x):
    print("404 Not Found: The uknown URL was requested.\n")
    return render_template("404.html"),404

#__________POSTS ______
@app.before_request
def beforerequest():
    if request.method == "POST":
        print("Post request recieved...")

# _________ROOT________
@app.route('/')
def welcome():
    print("\nWelcome page was requested.")
    return render_template("user/welcome.html")


#____________ SIGN UP _________________
@app.route('/signup',methods=["GET","POST"])
def signup():
     pass 

@app.route("/password",methods=["POST"])
def passwordsubmit():
    print("Password received")
    pass

#_____________login page____________
@app.route("/login")
def loging():
    if request.method == "POST":
        return render_template("login.html")
    else :
        return "<h1>hello world</h1>"



#__________ HOME ______________
@app.route('/home',methods=['POST','GET'])
def homepage():
    if request.method == "GET":
        if 'user' not  in session:
            return redirect('/login')
    
        if session['user']:
            return render_template("home.html")


# ____________BIN _____________________
@app.route('/bin')
def bin():
    return """
<div class="input-group">
  <input type="text" id="username" placeholder="Username" />
  <label for="username">Username</label>
</div>

                           
                           
                           """

# ---------------------Running the app if it is run as the main ---------------

if __name__ =="__main__":
    app.run(debug=True, host="0.0.0.0",port=9999)
