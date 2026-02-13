from flask import Flask, session, redirect, render_template,request, jsonify,flash
from flask_sqlalchemy import SQLAlchemy
from modules import HashGen
from modules import GenerateOTP
import json,os
from modules import CheckCooldown, SetCooldown , HashGen
from datetime import *
from concurrent.futures import ThreadPoolExecutor





POST = "POST"
DELETE = "DELETE"
GET = "GET"



# #############   APP CONFIGURATIONS ###########################
admin = Flask(__name__)
admin.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///admin/employees.db"
admin.config['SQLALCHEMY_BINDS'] = { 'dbadmin' :"sqlite:///admin/admin.db" }
db = SQLAlchemy(admin)
admin.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
admin.secret_key=os.urandom(24)




# ################ DATABASES ################

class RegisteredAdmins(db.Model):
  __bind_key__ = "dbadmin"
  __tablename__ = "admins"
  name = db.Column(db.String(256),nullable = False)
  username = db.Column(db.String(256),primary_key=True)
  password = db.Column(db.String(1000),nullable=False)
  email = db.Column(db.String(256),nullable=False)
  token = db.Column(db.String(256))

class RegisteringAdmins(db.Model):
  __bind_key__ = "dbadmin"
  __tablename__ = "registeringadmins"
  name = db.Column(db.String(256),nullable = False)
  username = db.Column(db.String(256),primary_key=True)
  password = db.Column(db.String(1000),nullable=False)
  email = db.Column(db.String(256),nullable=False)
  token = db.Column(db.String(256))
  verified = db.Column(db.Boolean,nullable=False,default = False)




with admin.app_context():
   db.create_all()
   # db.create_all(bind='dbadmin')
#____________________error handler_____________________________________
@admin.errorhandler(404)
def error(x):
   return render_template('404.html')

@admin.route('/')
def rootpage():
   print(db.session.get(RegisteredAdmins,"rahul").email)
   return render_template("admin/root.html")
#___________________________ Admin page _________________________________________
@admin.route('/admin')
def adminpage():
    if not session.get('admin'):
       return not_logged_in()

    if session.get('admin'):
        return render_template('admin/Admin.html')
    


#____________________________ADMIN REGISTRY________________________

@admin.route('/register', methods = ['GET','POST'])
def AdminRegister():
   
   if request.method=='GET':
      return render_template('admin/register.html')
      
   elif request.method == 'POST':
      register_pack = request.get_json()
      admin_name = register_pack.get('name',"").capitalize()
      admin_username = register_pack.get('username',"").lower()
      admin_email = register_pack.get('email',"").lower()
      admin_password = register_pack.get('password')
      admin_token = register_pack.get('token')
      admin_otp = register_pack.get('otp')
      admin_request_type = register_pack.get('request_type')
      print(admin_request_type)
      
      # Before requst of the html,...
      if admin_request_type == "onload_response":
         if not session.get("user"):
            return jsonify(response = "NewRegistration")
         elif session.get("user") and session.get("verified"):
            return jsonify(response = "SubmitDetails")
         elif session.get("user") and not session.get("verified"):
            return ("OtpVerification")

      # Requesting otp.
      elif admin_name and admin_email:
         if admin_request_type == "GenerateOtp":
            if session.get("verified") is True and session.get("user")== str(admin_email):
               return jsonify(status="verified")
            else:
               session['name'] = admin_name

               session['email'] = admin_email
               cooldown_time = session.get('cooldown')
               if cooldown_time is None:
                  
                  if not session.get("name"):
                     return jsonify(message="didnt get the name here")
                  reciever_email = session.get("email")
                  name =  session.get("name")
                  serverotp =  GenerateOTP(reciever_email,name)
                  session['serverotp'] = serverotp
                  print(session.get('now'))
                  
                  session['cooldown']= SetCooldown() 
                  print("cooldown has been set")
                  return jsonify(status="ok", message="Email has been sent.")

               elif CheckCooldown(session.get('cooldown')):
                  session['cooldown']= SetCooldown()
                  session[f"serverotp"] = GenerateOTP(session.get('email'),session.get("name"))
                  
                  return jsonify(status="ok", message="Email has been resent.")
               elif not CheckCooldown(session.get('cooldown')):
                  return jsonify(status="failed",message="The timer is under cooldown. please try again after sometime (Min cooldown : 30s)")
               else :
                  print("Sending mail failed")
                  return jsonify(message="failed")   
            
            ##submitting the otp;
      elif admin_otp:
         if str(admin_request_type) ==  str("SubmitOTP"):
            session["userotp"] = admin_otp
            if str(session.get('serverotp')) ==str (session.get("userotp")):
               session["verified"] = True
               session["user"]=admin_email
               
               session.pop("serverotp")
            else :
               return jsonify(message=f"Invalid OTP...!!!")
               
            

      elif admin_username and admin_password and admin_token:
         if admin_request_type == "SubmitDetails":
            print(admin_request_type)
            if session.get("verified") is False:
               return jsonify(status="NotVerified")
            session["username"] = admin_username
            session["password"] =  HashGen(admin_password)
            session["token"] = admin_token
            username = session.get("username")
            exists = RegisteredAdmins.query.filter_by(username=username).first()
            if exists:
               return jsonify(message="Username Exists. Choose another one.")
            
            elif str(exists) != str(username):
               dbusername = session.get("username")
               dbpassword = session.get("password")
               dbtoken = session.get("token")
               dbemail = session.get("email")
               dbname = session.get("name")
               NewUser = RegisteringAdmins(
                  username = dbusername, password = dbpassword , email = dbemail , token=dbtoken, name = dbname
               )
               try :
                  db.session.add(NewUser)
                  db.session.commit()
                  print("DB Session Success")
                  
                  return jsonify(status="dbsuccess")
                  # return redirect('/register/success')
               except Exception as e:
                  print("Error: Db session failed")
                  print(e)
                  return jsonify(message="An error occurred while setting the database. Please Try again.")
         else:
            return jsonify(message="")
            
      else :
         return jsonify(message="Empty Credentials..!!!")
         
 #_____________________ LOGIN___________________________
@admin.route('/login', methods=['GET','POST'])
def loginpage():
   if request.method == 'GET':
      return render_template("admin/admin_login.html")
   
   elif request.method == "POST":
      login_pack = request.get_json()
      username = login_pack.get("username")
      password = login_pack.get("password")
      user = db.session.get(RegisteredAdmins,username)
      if HashGen(password) == str(password):
         session['admin'] = username
      
      elif HashGen(password) != str(password):
         return jsonify(status = "failed",message = "Wrong Password")
      


         


        ######################################################
        #                   REDIRECTS                        #
        ######################################################
 # _________________________HOME REDIRECT_______________________________          
@admin.route('/home')
def adminhome():
    return redirect('/admin')

@admin.route('/signup')
def signup():
   return redirect("/register")

def not_logged_in():
   return render_template('notloggedin.html')


#### 

#--------------------XXXXXXXXXXXXXXXXXXX-------------------

@admin.route("/register/success")
def successs():
   return render_template("success.html")

@admin.route("/logout",methods=[POST])
def logout():
   data = request.get_json()
   if str(data.get("request_type")).strip()=="logout":
      session.clear()
      return jsonify(status="logout_ok",message="successfully logged out")
#______________PINGING THE SERVER__________

@admin.route("/ping",methods=['POST',"GET"])
def ping():
   return jsonify(ping="success")



#_____________________ ADMIN RUNNNNING ______________________
if __name__ == "__main__":
    print("\033[41mWarning: Please make sure that yo u have deleted the admin model\033[0m")
    admin.run(port=2222,debug=True,host='0.0.0.0')
    pass
