import unittest
from domain.Entites import *

class test_Student(unittest.TestCase):
    
    def test_update(self):
        stud = Student("Jhon")
        res = stud.test_activated(max_questions = 10)
        self.assertEqual(res<=10,True)
        
    def test_list_test_results(self):
        stud = Student("Jhon")
        result = Test_Results(5,10,'math')
        stud.add_test_results(result)
        self.assertEqual(stud.list_test_results(),[result])
    
    def test_list_marks(self):
        stud = Student("Jhon")
        mark = Mark(5,'math')
        stud.add_mark(mark)
        self.assertEqual(stud.list_marks(),[mark])