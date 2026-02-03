from flask import Flask,session,redirect,render_template,request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
test = Flask (__name__)
test.config['SQLALCHEMY_DATABASE_URI']="sqlite:///vijay.db"
test.config['SQLALCHEMY_BINDS']={
  'divya' : "sqlite:///admin.db"
}
db = SQLAlchemy(test)

class register(db.Model):
  __bind_key__ = "divya"
  username = db.Column(db.String(100),primary_key=True)
  password = db.Column(db.String(100),nullable=False)
  token = db.Column(db.String(100))
  
with test.app_context():
  db.create_all()
  

#_------------ routes-------------------
def unknown_request():
  return render_template('unknown.html'),501
  
@test.route('/')
def root():
  return render_template('root.html')

@test.route('/register', methods = ['GET','POST'])
def registerxx():
  if request.method=='GET':
    return render_template('register.html')
    
  elif request.method == 'POST':
    register_pack = request.get_json()
    print("got the data")
    admin_username = register_pack.get('username')
    admin_password = register_pack.get('password')
    admin_token = register_pack.get('token')
    with open('token.json','r',encoding='utf-8') as tokenkey:
      token = json.load(tokenkey)
      print("file opened   ",)
      print(f"{admin_token}    {token.get('token')}")

    if admin_token in token.get('token'):
      print("Yay!! token matched")
      NewAdmin = register(
        username = admin_username,
        password = admin_password,
        token = admin_token
      )
      exist = register.query.filter_by(username=admin_username).first()
      if not exist:
        try:
          db.session.add(NewAdmin)
          db.session.commit()
          return jsonify(message="db_success")
        except:
          print("failure error")
          return ("db failure")
      elif exist:
        print("user already exist.")
        return jsonify(message="the user exist")

      
    else :
      print("failure")
      return jsonify(message = "goodbye")


@test.route('/admin_login')
def admin():
  return render_template('admin_login.html')
  
  
if __name__ == '__main__':
  test.run(debug=True,port=1985,host='0.0.0.0')