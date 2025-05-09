import unittest
from domain.Entites import *
from domain.Test import *

class test_Test(unittest.TestCase):
    
    def test_active(self):
        stud_1 = Student("Jhon")
        stud_2 = Student("Kate")
        teacher = Teacher("Mr. Lewis",'math')
        test = Test('',teacher,10,[stud_1,stud_2])
        test.activate()
        self.assertEqual(len(test.test_results),2)
        
    def test_add_mark(self):
        stud_1 = Student("Jhon")
        stud_2 = Student("Kate")
        teacher = Teacher("Mr. Lewis",'math')
        test = Test('',teacher,10,[stud_1,stud_2])
        test.activate()
        test.add_test_results()
        self.assertEqual(len(stud_1.list_test_results()),1)
        mark_of_second_student = test.test_results[stud_2]
        self.assertEqual(stud_2.list_test_results(),[mark_of_second_student])        