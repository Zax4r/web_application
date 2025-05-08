import random
from .Mark import Mark
  

class Teacher:
    def __init__(self, name, subj):
        self.name = name
        self.subj = subj
           
    def update(self, message,**kwargs):
        pass

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []
    
    def test_activated(self,max_questions):
        return random.randint(1,max_questions)
    
    def add_mark(self,mark):
        self.marks.append(mark)
    
    def list_marks(self):
        return self.marks