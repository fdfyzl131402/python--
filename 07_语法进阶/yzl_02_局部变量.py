def demo1():
    # 定义一个局部变量
    # 1>出生： 当下方的代码被执行后，变量才会被创造
    # 2>死亡： 函数执行完成之后
    num = 10
    print("demo1函数内部的变量是%d" % num)


def demo2():
    pass
    # print(%d % num)
# 函数内部使用的变量不能在其他位置使用
# print("%s" % num)


demo1()
demo2()
