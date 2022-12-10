"""
判断字符串a="welcome to my world"是否包含单词b="world"包含返回True，不包含返回 False
"""
a = "welcome to my world"
b = "worlx"
if b in a:
    print(True)
else:
    print(False)

print(b in a)

print(a.find(b))

if a.find(b) == -1:
    print(False)
else:
    print(True)
# 三元表达式
print(False if a.find(b) == -1 else True)