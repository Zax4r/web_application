from flask import Flask, request, render_template, redirect, flash
from domain.TestingSystem import TestingSystem
import domain.utils as utils


app = Flask(__name__)
app.secret_key = "MYSECRETKEY"

loaded_system = utils.load()
testing_system = loaded_system if loaded_system else TestingSystem()

@app.route('/tests', methods=['GET', 'POST'])
def tests():
    if request.method == 'POST':
        title = request.form['title']
        max_questions = int(request.form['max_questions'])
        teacher_index = int(request.form['teacher_index'])
        testing_system.add_test(title, max_questions, teacher_index)
        
    
    teachers = testing_system.teachers
    tests = testing_system.tests
    return render_template('tests.html', teachers=teachers,tests=tests)

@app.route('/tests/<int:test_index>/activate', methods=['POST'])
def activate(test_index):
    testing_system.activate_test(test_index)
    testing_system.add_test_results(test_index)
    return redirect('/tests')

@app.route('/tests/<int:test_index>/convert', methods=['POST'])
def convert(test_index):
    testing_system.convert_test_results(test_index)
    return redirect('/tests')

@app.route('/tests/<int:test_index>/check', methods=['POST'])
def check(test_index):
    testing_system.put_marks(test_index)
    return redirect('/tests')

@app.route('/tests/<int:test_index>/delete', methods=['POST'])
def delete_test(test_index):
    testing_system.remove_test(test_index)
    return redirect('/tests')

@app.route('/', methods=['GET', 'POST'])
@app.route('/teachers',methods = ['GET','POST'])
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

@app.route('/teachers/<int:teacher_index>/delete', methods=['POST'])
def delete_teacher(teacher_index):
    testing_system.remove_teacher(teacher_index)
    return redirect('/teachers')

@app.route('/save')
def save():
    utils.save(testing_system)
    return redirect('/')
    
@app.route('/reviews',methods = ['GET','POST'])
def reviews():
    if request.method == "POST":
        author = request.form['author']
        text = request.form['text']
        testing_system.add_review(author,text)    
    
    reviews = testing_system.list_reviews()
    return render_template("reviews.html",reviews=reviews)

@app.route('/reviews/<int:review_index>/delete', methods=['POST'])
def delete_review(review_index):
    testing_system.remove_review(review_index)
    return redirect('/reviews')

@app.route('/students',methods = ['GET','POST'])
def students():
    if request.method == "POST":
        name = request.form['name']
        if utils.validate_name(name):
            testing_system.add_student(name)    
        else:
            flash("Имя не должно содержать цифр",category='warning')
    
    students = testing_system.students
    return render_template("students.html",students=students)

@app.route('/students/<int:student_index>/delete', methods=['POST'])
def delete_student(student_index):
    testing_system.remove_student(student_index)
    return redirect('/students')

if __name__ == '__main__':
    app.run(debug=True)