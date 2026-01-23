from flask import Flask, jsonify, request, session, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from otp import GenerateOTP
from signup import *




app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
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
    return render_template("welcome.html")


#____________ SIGN UP _________________
@app.route('/signup',methods=["GET","POST"])
def signup():
    if request.method == "GET":
        print(f"\n{request.method} :  Sign up page was requested")
        return render_template("signup.html")

    if request.method == "POST":
        payload = request.get_json()
        request_type = payload.get("request_type")
        
        #requesting the otp
        if request_type == "generateotp":
            email = payload.get("email")
            session['user'] = email
            session['otp'] = GenerateOTP(email)
            serverotp = session['otp']
            if serverotp :
                print("Response sent")
                return jsonify(message="otpsent")
            elif str(serverotp) =="Error_exception":
                print (f"\033[31m Error\033[0m : Unknown error has occurred...")
                return jsonify(message = "error")


            #submitting the otp
        if request_type == "submitotp":
            clientotp = payload.get("otp")
            serverotp = session.get('otp')
            if not serverotp:
                print("\033[31mError \033[0m: Variable holding the otp was not found")
            if str(serverotp) == str(clientotp):
                print("\nOTP Verification Successful")
                session.pop('otp',None)
                return jsonify(login="success", loginmessage="Login was succesfully verified by the server")
            else :
                print("OTP Verification failed")
                return jsonify(login="failed")

@app.route("/password",methods=["POST"])
def passwordsubmit():
    print("Password received")
    packet = request.get_json()
    request_type = request.get("request_type")
    if request_type == "Submit Password":
        RawPassword = packet.get("password")
        session['password']= HashGen(RawPassword)
    
        SignedUser =  SignedUsers(
            Email = session.get('user'),
            Password =  session.get('password')
    )
    try :
        db.session.add(SignedUser)
        db.session.commit()
        return jsonify(password_status = "successful", message="Password Save successful")

    except Exception as error:
        print(f"Error has occurred\n{error}")
        return jsonify(password_status="failed", message="Password save failed")


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
