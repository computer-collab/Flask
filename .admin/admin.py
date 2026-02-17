from config import ChangeRoot
ChangeRoot()


from flask import Flask, session, redirect, render_template,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash


admin = Flask(__name__)
admin.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///employees.db"
admin.config['SQLALCHEMY_BINDS'] = { 'dbadmin' :"sqlite:///admin.db" }
db = SQLAlchemy(admin)
admin.secret_key="he is an admin"

class AddEmployees(db.Model):
    Name = db.Column(db.String(1000),nullable=False)
    PhoneNo = db.Column(db.String(10),primary_key=True,unique=True)
    Email = db.Column(db.String(1000),primary_key=True)
    #Status = db.Column(db.Boolean, default=False)
class ManageEmployees(AddEmployees):
    pass 

class adminadd(db.Model):
    __bind_key__ = "dbadmin"
   
    __tablename__ = "admin"
    username = db.Column(db.String(100), nullable=False,primary_key=True)
    password = db.Column(db.String(100),nullable=False)


with admin.app_context():
    db.create_all()

@admin.route('/')
def main():
    return render_template("main.html")

@admin.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'GET' :
        return render_template('admin_login.html')
    
    if request.method == 'POST':
        data = request.get_json()
        usernamedata = data.get("username")
        passworddata = data.get("password")
        #dbuser = adminadd.query.filter_by(username =  usernamedata).first()
        if usernamedata == 'arun_tailors' :
            if passworddata == '12345678':
                session['logged_in'] =  True
                session['admin'] = usernamedata
                return jsonify(login = "success")
            else :
                return jsonify(login="failed", message = "Either Username or Password is incorrect")
        else :
            return jsonify(login="failed", message = "Either Username or Password is incorrect")


@admin.route('/admin')
def adminpage():
    if not session.get('admin'):
        
        return redirect('/login')
    if session.get('admin'):
        return render_template('Admin.html')
    
@admin.route('/addemployees')
def addemployes():
    if not session.get('admin'):
        return redirect('/login')
    
    if request.method == 'GET':
        return render_template('Add_employees.html')
    if request.method == 'POST':
        employee = request.get_json()
        if employee.request_type == "Submit Employee":
            
            email = employee.get('email')
            phonenumber = employee.get('phone_no')
            name = employee.get('name')

            NewEmployee = AddEmployees(
                
                Name = name , PhoneNo = phonenumber, Email = email )
            db.session.add(NewEmployee)
            db.session.commit()
            return jsonify(EmployeeStatus = "success")
        else :
            return jsonify(EmployeeStatus = "failed")
            

if __name__ == "__main__":
    print("\033[41mWarning: Please make sure that yo u have deleted the admin model\033[0m")




admin.run(port=2222,debug=True)