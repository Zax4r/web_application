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
        try:
            self.tests[index].activate(self.students)
        except Exception as e:
            print(e)

    def add_test_results(self,index:int):
        self.tests[index].add_test_results(self.students)
    
    def add_teacher(self,name,subj):
        self.teachers.append(Teacher(name,subj))
        
    def add_student(self,name):
        self.students.append(Student(name))
        
    def convert_test_results(self,index:int):
        try:
            test = self.tests[index]
            teacher = test.creator
            for student,test_result in test.test_results.items():
                mark = teacher.convert_test_results(test_result)
                student.add_mark(mark)
            self.tests.remove(test)
        except Exception as e:
            print(e)
    
    def add_review(self,author,text):
        self.review_handler.add(author,text)
        
    def list_reviews(self):
        return self.review_handler.list_reviews()