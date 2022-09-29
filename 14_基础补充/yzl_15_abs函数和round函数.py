# abs
print(abs(-10))
# round
print(round(1.2))
print(round(1.9))


# 需求： 对两个数字进行处理（取绝对值或四舍五入）


# 方法一
def add_num(a, b):
    return abs(a) + abs(b)


result = add_num(-1, 2)
print(result)


# 方法二
def sum_num(c, d, f):
    return f(c) + f(d)


print(sum_num(1.1, 1.6, round))