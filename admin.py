from flask import Flask, session, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

admin = Flask(__name__)
admin.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///employees.db"
db = SQLAlchemy(admin)
admin.secret_key="he is an admin"

class AddEmployees(db.Model):
    Name = db.Column(db.String(1000),nullable=False)
    PhoneNo = db.Column(db.String(10),primary_key=True,unique=True)
    Email = db.Column(db.String(1000),primary_key=True)
    #Status = db.Column(db.Boolean, default=False)



with admin.app_context():
    db.create_all()

if __name__ == "__main__":
    print("\033[41mWarning: Please make sure that yo u have deleted the admin model\033[0m")


admin.route("/")
def main():
    return render_template("main.html")

