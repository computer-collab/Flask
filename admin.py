from flask import Flask, session, redirect, render_template,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from modules.otp import GenerateOTP


admin = Flask(__name__)
admin.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///employees.db"
admin.config['SQLALCHEMY_BINDS'] = { 'dbadmin' :"sqlite:///admin.db" }
db = SQLAlchemy(admin)
admin.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
admin.secret_key="he is an admin"

#-----------------ADD EMPLOYEES=------------------------
class AddEmployees(db.Model):
    Name = db.Column(db.String(1000),nullable=False)
    PhoneNo = db.Column(db.String(10),primary_key=True,unique=True)
    Email = db.Column(db.String(1000),primary_key=True)
    VerifiedStatus = db.Column(db.Boolean, default=False,nullable=False)

# -------------- MANAGING EMPLOYEES -------------------------
class ManageEmployees(AddEmployees):
    pass 

# -------------- ADDING ADMINS ------------------------
class adminadd(db.Model):
    __bind_key__ = "dbadmin"
    username = db.Column(db.String(100), nullable=False,primary_key=True)
    password = db.Column(db.String(100),nullable=False)
#________________ CREATING DATABASE_______________________

with admin.app_context():
    db.create_all()
    # db.create_all(bind='dbadmin')

#___________________ ERROR HANDLER _____________________________
@admin.errorhandler(404)
def errorhandler(x):
    return render_template('404.html')

#___________________________ ROOT _____________________
@admin.route('/')
def main():
    return render_template("main.html")

# _________________________LOGIN ROUTE _______________________________
@admin.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'GET' :
        return render_template('admin_login.html')
    
    if request.method == 'POST':
        data = request.get_json()
        usernamejson = data.get("username")
        passwordjson= data.get("password")
        dbuser = adminadd.query.filter_by(username =  usernamejson).first()
        if  dbuser:
            print(dbuser)
            dbusername = dbuser.username
            if usernamejson == dbuser.username :
                print("Username verified")
                if dbuser.password == generate_password_hash(passwordjson):
                    session['logged_in'] =  True
                    session['admin'] = usernamejson
                    return jsonify(login = "success")
        elif usernamejson:
            print()
            # dbusername = dbuser.username
            if usernamejson == "aruntailors":
                print("Username verified manual")
                if passwordjson == '12345678':
                    session['logged_in'] =  True
                    session['admin'] = usernamejson
                    return jsonify(login = "success")
                else :
                    return jsonify(login="failed", message = "Either Username or Password is incorrect")
                
        else :
            print("Db user doesnt exist")
            return jsonify(login="failed", message = "Either Username or Password is incorrect")
        
    # ------------- NOT LOGGED IN ---------------------
@admin.route('/not_logged_in')
def not_logged_in():
    return render_template('notloggedin.html')

#___________________________ Admin page _________________________________________
@admin.route('/admin')
def adminpage():
    if not session.get('admin'):
       return not_logged_in()

    if session.get('admin'):
        return render_template('Admin.html')
    
@admin.route('/addemployees',methods=['POST','GET'])
def addemployees():
    if not session.get('admin'):
        return not_logged_in()
    
    if request.method == 'GET':
        return render_template('Add_employees.html')
    if request.method == 'POST':
        employee = request.get_json()
        print(employee)
        namejson = employee.get("name")
        email = employee.get('email')
        session['employeename']=namejson
        session['employeeemail']=email

        if employee.get("request_type") ==  "Generate otp":
            session['otp']=GenerateOTP(email,namejson)
            

        elif employee.get("request_type") ==  "Submit Employee":
            employee = request.get_json()
            phoneno = employee.get('phone_no')
            session['employeephoneno']=phoneno
            if session.get('otp') == employee.get('otp'): 
                pass

        return jsonify(EmployeeStatus = "success")

 # _________________________HOME REDIRECT_______________________________          
@admin.route('/home')
def adminhome():
    return redirect('/admin')
#_____________________ XXXXXXXXXXXXXX ______________________
if __name__ == "__main__":
    print("\033[41mWarning: Please make sure that yo u have deleted the admin model\033[0m")




admin.run(port=2222,debug=True)