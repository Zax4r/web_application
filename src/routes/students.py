from flask import Blueprint,render_template,request,redirect,flash
from app import testing_system
import domain.utils as utils

students_app = Blueprint("students","students",url_prefix='/students')

@students_app.route('/',methods = ['GET','POST'])
def students():
    if request.method == "POST":
        name = request.form['name']
        if utils.validate_name(name):
            testing_system.add_student(name)    
        else:
            flash("Имя не должно содержать цифр",category='warning')
    
    students = testing_system.students
    return render_template("students.html",students=students)

@students_app.route('/<int:student_index>/delete', methods=['POST'])
def delete_student(student_index):
    testing_system.remove_student(student_index)
    return redirect('/students')