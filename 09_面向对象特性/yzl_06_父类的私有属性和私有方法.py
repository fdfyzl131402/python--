class A:
    def __init__(self):
        self.num1 = 100
        # 私有属性
        self.__num2 = 200

    def __text(self):
        # 外界无法访问
        print("私有属性 %d %d" % (self.num1, self.__num2))

    def text(self):
        print("父类的公有方法 %d" % self.__num2)
        self.__text()


class B(A):

    def demo(self):

        # 1.子类的对象方法中无法访问父类的私有属性
        # print("访问父类的私有属性 %d " % self.__num2)

        # 2.在子类的对象方法中也不能调用父类的私有方法
        # self.__text()

        # 3.访问父类的公有属性
        print("访问父类的公有属性 %d " % self.num1)

        # 4.访问父类的共有方法
        self.text()


# 创建一个子类对象
b = B()
print(b)
b.demo()