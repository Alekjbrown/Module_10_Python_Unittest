import unittest

from pytest import approx

from Unit10.Topic3.classes import student

"""
Author: Alek Brown
Program: test_student.py
Date: 2021-04-13


Write unit test test_student_str(self)
Test the str() method
Write unit test test_object_not_created_error_last_name(self) that expect exception raised

Write a main() 
Create 2 student objects and print them
"""


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = student.Student('Hope', 'Bob', 'Speech', '3.6')

    def tearDown(self):
        del self.student

    def test_initial_value_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Hope')
        self.assertEqual(self.student.first_name, 'Bob')
        self.assertEqual(self.student.major, 'Speech')
        self.assertEqual(str(self.student.gpa), '3.6')

    def test_inital_all_attributes(self):
        person = student.Student('Brown', 'Ali', 'CIS', '3.8')  # this is not self.person from setUp, but local
        assert person.last_name == 'Brown'  # note no self here on person or assert
        assert person.first_name == 'Ali'
        assert person.major == 'CIS'
        assert person.gpa == '3.8'

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = student.Student('123', 'Ali', 'CIS', '3.6')

    def test_object_not_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            p = student.Student('Brown', '123', 'CIS', '3.6')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            p = student.Student('Brown', 'Ali', '123', '3.6')

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            p = student.Student('Brown', 'Ali', 'CIS', 'abc')

    def test_object_created_all_attributes(self):
        p = student.Student('Brown', 'Ali', 'CIS')
        assert p.last_name == 'Brown'
        assert p.first_name == 'Ali'
        assert p.major == 'CIS'
        assert p.gpa == approx(0.0)

    def test_person_str(self):
        self.assertEqual(str(self.student), 'Hope, Bob has major Speechwith gpa: 3.6')


if __name__ == '__main__':
    unittest.main()
