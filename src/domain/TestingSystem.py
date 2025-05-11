from .Entites import *
from .Test import *
from typing import List
from .Review import *

class TestingSystem:
    
    def __init__(self):
        self.students: List[Student] = []
        self.teachers: List[Teacher] = []
        self.tests: List[Test] = []
        self.review_handler = ReviewHandler()
    
    def add_test(self,title,max_questions,index: int):
        teacher = self.teachers[index]
        test = teacher.create_test(title,max_questions)
        self.tests.append(test)
    
    def activate_test(self,index: int):
        self.tests[index].activate(self.students)

    def add_test_results(self,index:int):
        self.tests[index].add_test_results(self.students)
    
    def add_teacher(self,name,subj):
        self.teachers.append(Teacher(name,subj))
        
    def add_student(self,name):
        self.students.append(Student(name))
        
    def convert_test_results(self,index:int):
        self.tests[index].convert_test_result_to_mark()
    
    def add_review(self,author,text):
        self.review_handler.add(author,text)
        
    def list_reviews(self):
        return self.review_handler.list_reviews()
    
    def put_marks(self,index):
        marks = self.tests[index].marks
        for student,mark in marks.items():
            student.add_mark(mark)
        self.remove_test(index)
    
    def remove_test(self,index):
        self.tests.pop(index)
        
    def remove_teacher(self,index):
        self.teachers.pop(index)
        
    def remove_student(self,index):
        self.students.pop(index)
        
    def remove_review(self,index):
        self.review_handler.remove(index)