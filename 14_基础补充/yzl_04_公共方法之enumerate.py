list1 = ["a", "b", "c", "d"]

# 返回结果是元组，元组第一个值是原迭代对象的数据的对应下标，第二个是原数据
# for i in enumerate(list1):
#     print(i)

for i in enumerate(list1, start=1):
    print(i)