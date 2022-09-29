# 定义类
class A(object):
    a = 0

    def __init__(self):
        self.b = 1


# 创建对象
aa = A()
# 调用__dict__
# 返回类的所有属性和方法的字典
print(A.__dict__)
# 返回实例属性和值的字典
print(aa.__dict__)
