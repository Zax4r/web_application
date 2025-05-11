from enum import Enum
from .Mark import Mark,Test_Results

class TestStates(Enum):
    Draft = 0
    Active = 1
    Completed = 2
    

class Test:
    def __init__(self, title, subj,max_questions):
        self.title = title
        self.max_questions = max_questions
        self.subj = subj
        self.state = TestStates.Draft.value
        self.test_results = {}
    
    def activate(self,students):
        if self.state == TestStates.Draft.value:
            self.state = TestStates.Active.value
            for student in students:
                answer = student.test_activated(self.max_questions)
                self.test_results[student] = Test_Results(answer,self.max_questions,self.subj)               
        self.state = TestStates.Completed.value
            
    def add_test_results(self,students):
        if self.state == TestStates.Completed.value:
            for student in students:
                if student in self.test_results.keys():
                    student.add_test_results(self.test_results[student])
                    
    
    def convert_test_result_to_mark(self,test_result):
        value = round(test_result.gained*10/test_result.max_possible)
        return Mark(value,test_result.subj)
    
    @property
    def is_draft(self):
        return self.state == TestStates.Draft.value
    
    def __eq__(self, value):
        return self.title == value.title