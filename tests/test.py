from flask import Flask, session, request, redirect
import threading
import time

app = Flask(__name__)
app.secret_key="He is an admin"
@app.route("/")
def root():
    return """
This is a root page
Please login
<button onclick="window.location.href ='/login'">Login</button>
"""
with app.app_context():
    def task()->None:
        pass

@app.route("/home")
def home():
    if not session.get("user"):
        return "please login"
    else :
    #     print("Thread started")
    #     time.sleep(30)
    #     print("Thread finished")
    #     session.pop("user")
    #     t = threading.Thread(target=task)
    #     t.start()
        if session.get("user"):
            # t.join()
            return """ This is home page
<button onclick="window.location.href='/logout'">Logout</button>
            """
        else :
            # t.join()
            return "error"
        
@app.route ("/login")
def login():
    if not session.get("user"):
        session["user"]="He is a user"
        return "Logged in"
    
    else :
        return redirect("/home")
    
@app.route("/logout")
def logout():
    session.clear()
    return "you are succress fuly logged out"





print("Main continues...")


if __name__ == "__main__":
    app.run(port=5555,host="0.0.0.0",debug=True)