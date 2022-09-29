# 计算列表中每个元素的二次方
list1 = [1, 2, 3, 4]


def func(x):
    return x ** 2


result = map(func, list1)
print(result)
print(list(result))