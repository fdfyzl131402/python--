xiaoming_dict = {"name": "小明"}

# 取值
print(xiaoming_dict["name"])

# 增加/修改
# 如果不存在，会新增键值对
xiaoming_dict["age"] = 18
# 如果存在，会修改键值对
xiaoming_dict["name"] = "小小明"
# 删除
xiaoming_dict.pop("name")

print(xiaoming_dict)