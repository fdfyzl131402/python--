import functools
list1 = [1, 2, 3, 4, 5]


# 定义功能函数
def functions(a, b):
    return a + b


result = functools.reduce(functions, list1)
print(result)