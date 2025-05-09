from flask import Flask, request, jsonify, render_template
from domain.TestingSystem import TestingSystem  # Adjust the import according to your module structure

app = Flask(__name__)
testing_system = TestingSystem()

@app.route('/', methods=['GET', 'POST'])
@app.route('/add_test', methods=['GET', 'POST'])
def add_test():
    if request.method == 'POST':
        title = request.form['title']
        max_questions = int(request.form['max_questions'])
        teacher_index = int(request.form['teacher_index'])
        testing_system.add_test(title, max_questions, teacher_index)
        
    
    teachers = testing_system.teachers
    return render_template('add_test.html', teachers=teachers)

@app.route('/add_teacher',methods = ['GET','POST'])
def add_teacher():
    if request.method == 'POST':
        name = request.form['name']
        subj = request.form['subj']
        testing_system.add_teacher(name,subj)

    teachers = testing_system.teachers
    return render_template('add_teacher.html',teachers=teachers)

if __name__ == '__main__':
    app.run(debug=True)