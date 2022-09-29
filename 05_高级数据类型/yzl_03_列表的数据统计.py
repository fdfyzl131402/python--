name_list = ["zhangsan", "lisi", "wangwu", "zhangsan"]

# len（长度）可以统计列表中元素的个数

list_len = len(name_list)
print("列表中包含%d个元素" % list_len)

# count 可以统计列表中某一个数据出现的次数
count = name_list.count("zhangsan")

print("zhangsan出现了%d次" % count)

# remove会删除列表中第一个出现的数据

name_list.remove("zhangsan")
print(name_list)
