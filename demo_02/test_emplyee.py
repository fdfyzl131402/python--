import unittest
from yzl_23_雇员 import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.yzl = Employee("余", "志龙", 20000)
        self.give_raise = [5000, 10000, 15000]

    def test_give_default_raise(self):
        self.yzl.give_raise(self.give_raise[0])
        self.assertIn(self.give_raise[0], self.give_raise)

    def test_give_custom_raise(self):
        self.yzl.give_raise(self.give_raise[1])
        self.assertIn(self.give_raise[1], self.give_raise)