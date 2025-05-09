import random
from .Mark import Mark,Test_Results
from typing import List
from .Test import Test

class Teacher:
    def __init__(self, name, subj):
        self.name = name
        self.subj = subj
           
    def create_test(self,title,students,max_questions):
        return Test(title,self,max_questions,students)
    
    def convert_test_results(self,test_results:Test_Results):
        value = round(test_results.gained/test_results.max_possible)
        return Mark(value,test_results.subj)

class Student:
    def __init__(self, name):
        self.name = name
        self.marks: List[Mark] = []
        self.test_results: List[Test_Results] = []
    
    def test_activated(self,max_questions):
        return random.randint(1,max_questions)
    
    def add_mark(self,mark):
        self.marks.append(mark)
    
    def add_test_results(self,test_result):
        self.test_results.append(test_result)
    
    def list_marks(self):
        return self.marks
    
    def list_test_results(self):
        return self.test_results