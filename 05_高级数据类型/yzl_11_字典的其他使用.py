xiaoming_dict = {"name": "小明",
                 "age": 18}

# 统计键值对数量
print(len(xiaoming_dict))
# 合并字典
temp_dict = {"height": 1.75,
             "age": 20}
# 如果字典中已有的键再次出现会被覆盖
xiaoming_dict.update(temp_dict)

# 清空字典
# xiaoming_dict.clear()
print(xiaoming_dict)