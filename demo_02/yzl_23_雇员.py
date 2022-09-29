class Employee(object):
    """储存姓名和年薪，年薪增加函数用于不同人的年薪变化"""
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, add=''):
        """年薪变化分两种情况"""
        if add:
            self.salary += add
        else:
            self.salary += 5000
        return self.salary


yzl = Employee("余", "志龙", 20000)
print(yzl.give_raise())
