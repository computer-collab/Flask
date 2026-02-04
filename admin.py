from flask import Flask, session, redirect, render_template,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from modules.otp import GenerateOTP
import json
from modules.time import CheckCooldown, SetCooldown
from datetime import *










# #############   APP CONFIGURATIONS ###########################
admin = Flask(__name__)
admin.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///admin/employees.db"
admin.config['SQLALCHEMY_BINDS'] = { 'dbadmin' :"sqlite:///admin/admin.db" }
db = SQLAlchemy(admin)
admin.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
admin.secret_key="he is an admin"



# ################ DATABASES ################



#___________________________ Admin page _________________________________________
@admin.route('/admin')
def adminpage():
    if not session.get('admin'):
       return not_logged_in()

    if session.get('admin'):
        return render_template('Admin.html')
    

class register(db.Model):
  __bind_key__ = "divya"
  username = db.Column(db.String(100),primary_key=True)
  password = db.Column(db.String(100),nullable=False)
  token = db.Column(db.String(100))

#____________________________ADMIN REGISTRY________________________

@admin.route('/register', methods = ['GET','POST'])
def AdminRegister():
  if request.method=='GET':
    return render_template('register.html')
    
  elif request.method == 'POST':
     register_pack = request.get_json()
     admin_name = register_pack.get('name')
     admin_username = register_pack.get('username')
     admin_email = register_pack.get('email')
     admin_password = register_pack.get('password')
     admin_token = register_pack.get('token')
     admin_otp = register_pack.get('otp')
     admin_request_type = register_pack.get('request_type')

     # Requesting otp.
     if admin_request_type == "GenerateOtp":
        session['email'] = admin_email
        session['otp'] = GenerateOTP(admin_email)
        session['now'] = datetime.now()
        otp =  GenerateOTP(session.get['email'])
        session['cooldown'] = SetCooldown(session.get('now')) #setting the cooldown
        return jsonify(status="ok", message="Email has been sent.")

     if CheckCooldown(session.get('cooldown')):
         pass 
           
           


        

 # _________________________HOME REDIRECT_______________________________          
@admin.route('/home')
def adminhome():
    return redirect('/admin')
#_____________________ ADMIN RUNNNNING ______________________
if __name__ == "__main__":
    print("\033[41mWarning: Please make sure that yo u have deleted the admin model\033[0m")
    admin.run(port=2222,debug=True,host='0.0.0.0')