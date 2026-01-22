from flask import Flask, jsonify, request, session, render_template
from flask_sqlalchemy import SQLAlchemy
from otp import GenerateOTP


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db = SQLAlchemy(app)


# =-------- DATABASES ------------------------

#__________USERS SIGNUP _______________________

class SignedUsers(db.Model):
    Email = db.Column(db.String(1000),nullable = False)
    PhoneNo = db.Column(db.String(10),primary_key=True, nullable=False)
    Password = db.Column(db.String(1000), primary_key=False, nullable=False)


#--------- CREATING THE DATA BASE -----------
with app.app_context():
    db.create_all()
    


#----------- ROUTES --------------
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
        if payload.request_type == "generateotp":
            email = payload.get(email)
            
            otp = GenerateOTP(email)
            if otp :
                return jsonify(message="OTP Sent")
            else return jsonify(message="not sent")



# ---------------------Running the app if it is run as the main ---------------

if __name__ =="__main__":
    app.run(debug=True, host="0.0.0.0",port=9999)
