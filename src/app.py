from flask import Flask, request, render_template, redirect, flash
from domain.TestingSystem import TestingSystem
import domain.utils as utils


app = Flask(__name__)
app.secret_key = "MYSECRETKEY"

loaded_system = utils.load()
testing_system = loaded_system if loaded_system else TestingSystem()

@app.route('/')
def index():
    return redirect('/teachers')

@app.route('/save')
def save():
    utils.save(testing_system)
    return redirect('/')

from routes.teachers import teachers_app
from routes.students import students_app
from routes.reviews import reviews_app
from routes.tests import tests_app


app.register_blueprint(students_app)
app.register_blueprint(reviews_app)
app.register_blueprint(teachers_app)
app.register_blueprint(tests_app)
