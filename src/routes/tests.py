from flask import Blueprint,render_template,request,redirect,flash
from app import testing_system
import domain.utils as utils

tests_app = Blueprint("tests","tests",url_prefix='/tests')





@tests_app.route('/', methods=['GET', 'POST'])
def tests():
    if request.method == 'POST':
        title = request.form['title']
        max_questions = int(request.form['max_questions'])
        teacher_index = int(request.form['teacher_index'])
        testing_system.add_test(title, max_questions, teacher_index)
        
    
    teachers = testing_system.teachers
    tests = testing_system.tests
    return render_template('tests.html', teachers=teachers,tests=tests)

@tests_app.route('/<int:test_index>/activate', methods=['POST'])
def activate(test_index):
    testing_system.activate_test(test_index)
    testing_system.add_test_results(test_index)
    return redirect('/tests')

@tests_app.route('/<int:test_index>/convert', methods=['POST'])
def convert(test_index):
    testing_system.convert_test_results(test_index)
    return redirect('/tests')

@tests_app.route('/<int:test_index>/check', methods=['POST'])
def check(test_index):
    testing_system.put_marks(test_index)
    return redirect('/tests')

@tests_app.route('/<int:test_index>/delete', methods=['POST'])
def delete_test(test_index):
    testing_system.remove_test(test_index)
    return redirect('/tests')