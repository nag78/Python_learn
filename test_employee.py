import unittest
from Employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        first = 'staff'
        last = 'staffovich'
        self.cust_give = 4500
        self.my_raise = Employee(first,last)

    def test_give_default_raise(self):
        """проверка стандартной прибавки к окладу"""


        self.assertEqual(self.my_raise.give_raise(),40000)
    def test_give_custom_raise(self):
        """проверка custom прибавки"""
        new_salary = self.my_raise.give_raise(self.cust_give)
        self.assertEqual(new_salary,39500)
unittest.main()