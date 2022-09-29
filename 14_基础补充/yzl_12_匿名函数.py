# 需求：函数 返回 100
def fn1():
    return 100


fn1()
print(fn1())

# lambda 匿名函数
fn2 = lambda: 100
print(fn2)  # 返回的是fn2的地址

# 调用函数 返回值
print(fn2())


# 需求：计算任意两个数相加的和

def add(a, b):
    return a + b


result = add(1, 2)
print(result)

# 匿名函数实现
sum = lambda a, b: a + b
print(sum(1, 2))