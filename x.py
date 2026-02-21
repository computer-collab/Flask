from routes.employees import employee
from flask import *
app = Flask(__name__)

app.register_blueprint(employee)
app.run()