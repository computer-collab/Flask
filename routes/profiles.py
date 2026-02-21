from flask import Blueprint, jsonify, render_template, request, redirect, session, url_for

# from Models import db, Employees
POST = "POST"
GET = "GET"


profiles_bp = Blueprint('profiles', __name__, template_folder='templates')
@profiles_bp.route('/profile/<username>')
def profile(username):
    # In a real application, you would fetch user data from a database
    user_data = {
        'username': username,
        'full_name': 'John Doe',
        'bio': 'Software developer and tech enthusiast.',
        'profile_picture': url_for('static', filename='images/default_profile.png')
    }
    return jsonify(user_data)
@profiles_bp.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if not session.get("admin"):
        return redirect("/admin_login")
    if request.method == GET:
        return render_template('admin/add_employees.html')
    elif request.method == POST:
        employee_pack =  request.get_json()
        employee_name= employee_pack.get('name')
        employee_phone_number = employee_pack.get('phone_number')
        employee_email_address = employee_pack.get('email_address')
        employee_worker_type = employee_pack.get('worker_type')
        
@profiles_bp.route('/helloworld')
def helloworld():
    return "Hello, World!"