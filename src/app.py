from flask import Flask, request, render_template, redirect
from domain.TestingSystem import TestingSystem
import domain.utils as utils


app = Flask(__name__)
loaded_system = utils.load()
testing_system = loaded_system if loaded_system else TestingSystem()

@app.route('/tests', methods=['GET', 'POST'])
def tests():
    if request.method == 'POST':
        try:
            title = request.form['title']
            max_questions = int(request.form['max_questions'])
            teacher_index = int(request.form['teacher_index'])
            testing_system.add_test(title, max_questions, teacher_index)
        except Exception as e:
            print(e)
        
    
    teachers = testing_system.teachers
    tests = testing_system.tests
    return render_template('tests.html', teachers=teachers,tests=tests)

@app.route('/', methods=['GET', 'POST'])
@app.route('/teachers',methods = ['GET','POST'])
def teachers():
    if request.method == 'POST':
        try:
            name = request.form['name']
            subj = request.form['subj']
            testing_system.add_teacher(name,subj)
        except Exception as e:
            print(e)

    teachers = testing_system.teachers
    return render_template('teachers.html',teachers=teachers)

@app.route('/save')
def save():
    utils.save(testing_system)
    return redirect('/')
    

@app.route('/students',methods = ['GET','POST'])
def students():
    if request.method == "POST":
        name = request.form['name']
        testing_system.add_student(name)    
    
    students = testing_system.students
    return render_template("students.html",students=students)

if __name__ == '__main__':
    app.run(debug=True)