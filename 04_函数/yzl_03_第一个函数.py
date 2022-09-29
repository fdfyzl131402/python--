name = "小明"

# 解释器知道这里定义了一个函数


def say_hello():
    """打招呼"""
    print("hello 1")

    print("hello 1")

    print("hello 1")


print(name)

# 只有调用函数时之前定义的函数才能执行
# 函数执行之后，继续执行后续的函数
say_hello()

print(name)
