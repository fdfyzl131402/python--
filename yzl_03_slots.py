class Students(object):
    __slots__ = ('name', 'age')

    def __init__(self, x, y):
        self.name = x
        self.age = y

    def say_hello(self):
        print(f"我是{self.name},{self.age}岁")


s1 = Students("jack", 18)
s1.say_hello()
