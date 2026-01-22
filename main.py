from flask import Flask, jsonify, request, session, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from otp import GenerateOTP




app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db = SQLAlchemy(app)
app.secret_key = "this is ultra long secret code"

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
        request_type = payload.get("request_type")
        
        #requesting the otp
        if request_type == "generateotp":
            email = payload.get("email")
            
            session['otp'] = GenerateOTP(email)
            serverotp = session['otp']
            if serverotp :
                print("Response sent")
                return jsonify(message="otpsent")
            else : print("respose not sent");return jsonify(message="otpnotsent")


            #submitting the otp
        if request_type == "submitotp":
            clientotp = payload.get("otp")
            serverotp = session.get('otp')
            if not serverotp:
                print("error server otp variable not found")
            if str(serverotp) == str(clientotp):
                print("\nOTP Verification Successful")
                session.pop('otp',None)
                return jsonify(login="success", loginmessage="Login was succesfully verified by the server")
            else :
                print("OTP Verification failed")
                return jsonify(login="failed")




# ---------------------Running the app if it is run as the main ---------------

if __name__ =="__main__":
    app.run(debug=True, host="0.0.0.0",port=9999)
