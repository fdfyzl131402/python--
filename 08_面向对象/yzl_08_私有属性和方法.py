class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # 私有属性是可以在方法内部被访问的
        print("%s的年龄是%d" % (self.name, self.__age))


xiaofang = Women("小芳")
# 伪私有属性在外部不能被访问
# xiaofang.__age()
print(xiaofang._Women__age)
# 伪私有方法同样不允许在外部被访问
# xiaofang.secret()
xiaofang._Women__secret()
