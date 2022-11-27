"""找出单词“welcome”在字符串"Hello,welcome to my world.”中出现的位置，
找不到返回-1
从下标0开始索引
"""
a = "Hello,welcome to my world."

print(a.index("w"))

print(a.index("welcome"))
print(a.index("e", 5, 10))

if "welcome" in a:
    print(a.index("e", 5, 10))
else:
    print(-1)

print(a.index("e", 5, 10) if "welcome" else -1)