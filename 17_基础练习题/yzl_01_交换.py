"""
已知a = "hello", b = "world",将其交换，使之 a = "world" , b = "hello"
"""
# 中间变量
a = "hello"
b = "world"
c = a
a = b
b = c
print(a, b)

# 2.推荐方法
a, b = b, a
print(a, b)