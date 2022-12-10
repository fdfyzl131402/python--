# 输入一个姓名，判断是否姓王
a = input("请输入一个姓名")

if a.endswith("哈"):
    print(True)

else:
    print(False)

print(True if a.startswith("王") else False)
