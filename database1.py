from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 
db = SQLAlchemy()


class User(db.Model):
    __tablename__="chitti"
    username = db.Column(db.String(1000), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)


def insert_user():
    username = input("Enter username: ").strip()
    name = input("Enter name: ").strip()
    age_input = input("Enter age: ").strip()

    if not age_input.isdigit():
        print("Age must be a number.")
        return

    user = User(username=username,name=name, age=int(age_input))
    db.session.add(user)
    db.session.commit()
    print("User inserted successfully.\n")


def query_users():
    username = input("Enter the query wanted to query:   ")
    
    users = db.session.get(User,username)
    print(f"The first prior\nID: {users.username} | Name: {users.name} | Age: {users.age}\n")
  


    if not users:
        print("No users found.\n")
        return

    print("\nStored Users:")

    if True:
        print(f"ID: {user.username} | Name: {user.name} | Age: {user.age}")
    print()


def main():
    while True:
        print("Choose an option:")
        print("1 - Insert data")
        print("2 - Query data")
        print("3 - Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            insert_user()
        elif choice == "2":
            query_users()
        elif choice == "3":
            print("Exiting.")
            break
        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Auto-creates database and tables
        main()
