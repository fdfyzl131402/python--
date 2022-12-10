"""
输出指定字符串A在字符串B中第一次出现的位置,如果B中不包含A,则输出-1
从О开始计数
A= "hello"
= "hi how are you hello world, hello yoyo !"
"""

a = "hello"
b = "hi how are you hello world, hello yoyo !"
print(b.find(a, 16, 28))

try:
    print(b.index(a))
except:
    print(-1)
