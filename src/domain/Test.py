from enum import Enum
from .Mark import Mark,Test_Results

class TestStates(Enum):
    Draft = 0
    Tested = 1
    Completed = 2
    

class Test:
    def __init__(self, title, subj,max_questions):
        self.title = title
        self.max_questions = max_questions
        self.subj = subj
        self.state = TestStates.Draft.value
        self.test_results = {}
        self.marks = {}
    
    def activate(self,students):
        if self.state == TestStates.Draft.value:
            for student in students:
                answer = student.test_activated(self.max_questions)
                self.test_results[student] = Test_Results(answer,self.max_questions,self.subj)               
        self.state = TestStates.Tested.value
            
    def add_test_results(self,students):
        if self.state == TestStates.Tested.value:
            for student in students:
                if student in self.test_results.keys():
                    student.add_test_results(self.test_results[student])
                    
    
    def convert_test_result_to_mark(self):
        self.state = TestStates.Completed.value
        for student,test_result in self.test_results.items():
            value = round(test_result.gained*10/test_result.max_possible)
            self.marks[student] = Mark(value,self.subj)
    
    
    
    @property
    def is_draft(self):
        return self.state == TestStates.Draft.value
    
    @property
    def is_tested(self):
        return self.state == TestStates.Tested.value
    
    def __eq__(self, value):
        return self.title == value.title