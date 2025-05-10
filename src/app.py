from flask import Flask, request, jsonify, render_template
from domain.TestingSystem import TestingSystem

app = Flask(__name__)
testing_system = TestingSystem()

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
        
    
    teachers = testing_system.all_teachers
    tests = testing_system.all_tests
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

    teachers = testing_system.all_teachers
    return render_template('teachers.html',teachers=teachers)

@app.route('/students',methods = ['GET','POST'])
def students():
    if request.method == "POST":
        name = request.form['name']
        testing_system.add_student(name)    
    
    students = testing_system.all_students
    return render_template("students.html",students=students)

if __name__ == '__main__':
    app.run(debug=True)