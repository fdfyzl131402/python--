a = 6
b = 100

# # 解法一 - 使用其他变量
# c = a
# a = b
# b = c
# print(a)
# print(b)

# 揭发二 - 不使用任何其他变量
# a = a + b
# b = a - b
# a = a - b
# print(a)
# print(b)

# 解法三 - python专用
# 等号右边是一个元组，省略括号
a, b = b, a
print(a)
print(b)