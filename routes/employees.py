from Models import *
from flask import Flask, jsonify, request, session, render_template, redirect, Blueprint

employee = Blueprint('employe',__name__,url_prefix="/profiles/employees")
@employee.route("/helloworld")
def helloworld():
    return "helloworld"