from enum import Enum
from .Mark import Mark,Test_Results

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
        self.test_results = {}
    
    def activate(self):
        if self.state == TestStates.Draft.value:
            self.state = TestStates.Active.value
            for student in self.students:
                answer = student.test_activated(self.max_questions)
                self.test_results[student] = Test_Results(answer,self.max_questions,self.subj)               
        self.state = TestStates.Completed.value
            
    def add_test_results(self):
        if self.state == TestStates.Completed.value:
            for student in self.students:
                student.add_test_results(self.test_results[student])