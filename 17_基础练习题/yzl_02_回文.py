"""
回文的定义:"回文"就是正读倒读都一样的。
如奇数个:"98789"，这个数字正读是"98789”倒读也是"98789"。
偶数个数字"3223"也是回文数。
字母"abcba"也是回文。
判断一个字符串是否是回文字符串，是打印True，不是打印False
"""

# 1. 切片
a = "abcba"
# if a[:2] == a[4:2:-1]:
#     print("true")
print(a == a[::-1])

# 2. reversed反转
# b = reversed(a)
# c = "".join(b)
# print(a == c)
print(a == "".join(reversed(a)))

