# 无参数
fn1 = lambda: 100
print(fn1())

# 一个参数
fn2 = lambda a: a
print(fn2("hello"))

# 默认参数 / 缺省参数
fn3 = lambda a, b, c= 100: a + b + c
print(fn3(10, 20))

# *args   元组
fn4 = lambda *args: args
print(fn4(10, 20, 30))

# **kwargs   返回字典
fn5 = lambda **kwargs: kwargs
print(fn5(name="tom", age=18))

# 带判断的lambda 应用
fn6 = lambda a, b: a if a > b else b
print(fn6(1000, 500))  