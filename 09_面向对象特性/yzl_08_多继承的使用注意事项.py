class A:

    def test(self):
        print("A ---text方法")

    def demo(self):
        print("A ---demo方法")


class B:

    def demo(self):
        print("B ---demo方法")

    def test(self):
        print("B ---text方法")


class C(A, B):
    """同时具有多个父类的方法和属性"""
    pass


# 创建子类对象
c = C()
c.test()
c.demo()

# 确定C类对象调用方法的顺序
print(C.__mro__)