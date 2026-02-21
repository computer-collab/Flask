#DEFAULTS
from flask import Flask, session, redirect, render_template,request, jsonify,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import *
import json,os

#HANDMADE
from modules import HashGen,GenerateOTP,VerifyCredentials,CheckCooldown, SetCooldown , HashGen
from Models import db, register
from routes.profiles import profiles_bp




OK = "ok"
POST = "POST"
DELETE = "DELETE"
GET = "GET"



# #############   APP CONFIGURATIONS ###########################
admin = Flask(__name__)
admin.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///admin/employees.db"
admin.config['SQLALCHEMY_BINDS'] = { 
   'dbadmin' :"sqlite:///admin/admin.db",
   "employees" :  "sqlite:///admin/employees/employees.db"
                                     }
admin.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
admin.secret_key=os.urandom(24)
db.init_app(admin)



# ################ DATABASES ################



with admin.app_context():
   db.create_all()
   # db.create_all(bind='dbadmin')
#____________________error handler_____________________________________
@admin.errorhandler(404)
def error(x):
   return render_template('404.html')

@admin.route('/')
def rootpage():
   return render_template("admin/root.html")
#___________________________ Admin page _________________________________________
@admin.route('/admin')
def adminpage():
    if not session.get('admin'):
       return not_logged_in()

    if session.get('admin'):
        return render_template('admin/Admin.html')
    


#____________________________ADMIN REGISTRY________________________

@admin.route('/add_admin', methods = ['GET','POST'])
def AdminRegister():
   #Temporarily downing the register page
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
      admin_pack = [admin_name,admin_password, admin_email,  admin_token,admin_username]
      

      # Requesting otp.
      if admin_name and admin_email:
         if admin_request_type == "GenerateOtp":
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
               return jsonify(status=OK, message="Email has been sent.")

            elif CheckCooldown(session.get('cooldown')):
               session['cooldown']= SetCooldown()
               session[f"serverotp"] = GenerateOTP(session.get('email'),session.get("name"))
               
               return jsonify(status=OK, message="Email has been resent.")
            elif not CheckCooldown(session.get('cooldown')):
               return jsonify(status="failed",message="The timer is under cooldown. please try again after sometime (Min cooldown : 30s)")
            else :
               print("Sending mail failed")
               return jsonify(message="failed")   
      
      elif admin_username and admin_password and admin_token:
         if admin_request_type == "SubmitDetails":
            print(admin_request_type)
            session["userotp"] = admin_otp
            session["username"] = admin_username
            session["password"] =  HashGen(admin_password)
            session["token"] = admin_token
            if str(session.get('serverotp')) ==str (session.get("userotp")):
               session.pop("serverotp")
               
               session["verified"] = True
               username = session.get("username")
               exists = register.query.filter_by(username=username).first()
               if exists:
                  return jsonify(message="Username Exists. Choose another one.")
               
               elif str(exists) != str(username):
                  dbusername = session.get("username")
                  dbpassword = session.get("password")
                  dbtoken = session.get("token")
                  dbemail = session.get("email")
                  dbname = session.get("name")
                  NewUser = register(
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
               
               return jsonify(message=f"Invalid OTP...!!!")
            
      else :
         return jsonify(message="Empty Credentials..!!!")
#___________modifying the admin registration exp____________
@admin.route("/register/verification",methods=[POST,GET])
def registerVerification():
   if True:
      return jsonify(message="ok")
 #_____________________ LOGIN___________________________
@admin.route('/admin_login', methods=['GET','POST'])
def loginpage():
   if request.method == 'GET':
      return render_template("admin/admin_login.html")
         
   elif request.method == "POST":
      print("post request recieved from the client")
      login_pack = request.get_json()
      admin_username = login_pack.get("username")
      admin_password = login_pack.get("password")
      server_pack = register.query.filter_by(username=admin_username).first()
      print("Sending the post from server...")
      if  server_pack:
         if VerifyCredentials(server_pack.password,admin_password):
            session["admin"]=admin_username
            session["loggedin"]=True
            return jsonify(status=OK,message="Credentials has been verified")
         else :
            return jsonify(message=f"{server_pack.password}\n {admin_password}")
         return jsonify(message=f"{server_pack.username}  {server_pack.password}")
      elif server_pack is None:
         print("Usernot found")
         return jsonify(status = "fail", message = "User Not found")
      return jsonify(status=OK,message="login success ful")
      
         
## ________________ADD_EMPLOYEES_____________________________
@admin.route('/add_employees',methods=[POST,GET])
def add_employees():
   if not session.get("admin"):
      return redirect("/admin_login")
   else:
      if request.method == GET:
         return render_template("admin/add_employees.html")
      elif request.method == POST:
         detail_pack=request.get_json()
         pass

      

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
#______________PINGING THE SERVER__________

@admin.route("/ping",methods=['POST',"GET"])
def ping():
   return jsonify(ping="success")
#_____________________REGISTER BLUEPRINT___________________________
admin.register_blueprint(profiles_bp)
#_____________________ ADMIN RUNNNNING ______________________
if __name__ == "__main__":
    admin.run(port=2222,debug=True,host='0.0.0.0')
    pass
