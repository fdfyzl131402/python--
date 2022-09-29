# 1.循环实现
# list1 = []
# i = 0
# while i < 10:
#     list1.append(i)
#     i += 1
#
# print(list1)

# for 实现 ------------
# for i in range(0, 10):
#     list1.append(i)
#
# print(list1)

# 列表推导式实现
# list1 = [i for i in range(10)]
# print(list1)

# 带range步长
list1 = [i for i in range(0, 10, 2)]
print(list1)

# for循环加if判断实现
list2 = []
for i in range(10):
    if i % 2 == 0:
        list2.append(i)

print(list2)

# 带if的推导式实现
list3 = [i for i in range(10) if i % 2 == 0]
print(list3)

# [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# 普通循环实现
list4 = []
for i in range(1, 3):
    for j in range(3):
        list4.append((i, j))

print(list4)

# 多个for实现列推导式
list5 = [(i, j)for i in range(1, 3) for j in range(3)]
print(list5)

