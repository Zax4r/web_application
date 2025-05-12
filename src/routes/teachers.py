from flask import Blueprint,render_template,request,redirect,flash
from app import testing_system
import domain.utils as utils

teachers_app = Blueprint("teachers","teachers",url_prefix='/teachers')

@teachers_app.route('/',methods = ['GET','POST'])
def teachers():
    if request.method == 'POST':
        
        name = request.form['name'].strip()
        subj = request.form['subj'].strip()
        if utils.validate_name(name) and utils.validate_name(subj):
            testing_system.add_teacher(name,subj)
        else:
            flash("Не должны содержать цифр",category='warning')

    teachers = testing_system.teachers
    return render_template('teachers.html',teachers=teachers)

@teachers_app.route('/<int:teacher_index>/delete', methods=['POST'])
def delete_teacher(teacher_index):
    testing_system.remove_teacher(teacher_index)
    return redirect('/teachers')