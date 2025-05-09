import unittest
from domain.TestingSystem import *

class test_Testing_System(unittest.TestCase):
    
    def test_adding_functions(self):
        system = TestingSystem()

        system.add_student("Jhon")
        system.add_teacher("Mr. Lewis",'math')
        self.assertEqual(system.students[0].name,"Jhon")
        self.assertEqual(system.teachers[0].name,"Mr. Lewis")
        