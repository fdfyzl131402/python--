class A:

    def test(self):
        print("text方法")


class B:

    def demo(self):
        print("demo方法")


class C(A, B):
    """同时具有多个父类的方法和属性"""
    pass


# 创建子类对象
c = C()
c.test()
c.demo()
