from enum import Enum
from .Mark import Mark

class TestStates(Enum):
    Draft = 0
    Active = 1
    Completed = 2
    

class Test:
    def __init__(self, title, teacher,max_questions,students = None):
        self.title = title
        self.creator = teacher
        self.max_questions = max_questions
        self.subj = teacher.subj
        self.students = students if students else []
        self.state = TestStates.Draft.value
        self.marks = {}
    
    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
    
    def unsubscribe(self, subscriber):
        self.students.remove(subscriber)
    
    def activate(self):
        if self.state == TestStates.Draft.value:
            self.state = TestStates.Active.value
            for student in self.students:
                answer = student.test_activated(self.max_questions)
                self.marks[student] = Mark(answer,self.subj)               
        self.state = TestStates.Completed.value
            
    def add_mark(self):
        if self.state == TestStates.Completed.value:
            for student in self.students:
                student.add_mark(self.marks[student])