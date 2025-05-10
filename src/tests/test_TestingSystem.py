import unittest
from domain.TestingSystem import *

class test_Testing_System(unittest.TestCase):
    
    def test_adding_functions(self):
        system = TestingSystem()

        system.add_student("Jhon")
        system.add_teacher("Mr. Lewis",'math')
        self.assertEqual(system.students[0].name,"Jhon")
        self.assertEqual(system.teachers[0].name,"Mr. Lewis")
    
    def test_activate_test(self):
        system = TestingSystem()

        student1 = Student('Jhon')
        student2 = Student("Mike")
        teacher = Teacher("Mr. Lewis",'math')
        system.students.extend([student1,student2])
        system.teachers.append(teacher)
        
        system.add_test("New Test",10,0)
        system.activate_test(0)
        system.add_test_results(0)
        
        self.assertEqual(len(student1.list_test_results()),1)
        self.assertEqual(len(student1.list_marks()),0)
        self.assertEqual(len(student2.list_test_results()),1)
        self.assertEqual(len(student2.list_marks()),0)
        
        system.convert_test_results(0)
        
        self.assertEqual(len(student1.list_test_results()),1)
        self.assertEqual(len(student1.list_marks()),1)
        self.assertEqual(len(student2.list_test_results()),1)
        self.assertEqual(len(student2.list_marks()),1)

