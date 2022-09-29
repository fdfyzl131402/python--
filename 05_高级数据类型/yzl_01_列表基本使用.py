name_list = ["zhangsan", "lisi", "wangwu"]

# 取值和取索引
print(name_list[0])

print(name_list.index("zhangsan"))
# 修改
name_list[1] = "李四"
# 增加
# 在列表末尾增加数据
name_list.append("王小二")
# 在列表的制定索引位置插入数据
name_list.insert(1, "yzl")
# 把其他列表的完整数据追加到当前列表的末尾
temp_list = ["孙悟空", "猪八戒", "沙师弟"]
name_list.extend(temp_list)
# 删除
# 从列表中删除指定的数据
name_list.remove("wangwu")
# pop默认删除元素最后一个
name_list.pop()
# 可以指定要删除元素的索引
name_list.pop(3)
# 清空列表所以元素
# name_list.clear()
print(name_list)
