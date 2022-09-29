# k ：i , v : i **2
dict1 = {i: i**2 for i in range(1, 5)}
print(dict1)

list1 = ["name", "age", "gender", "id"]
list2 = ["tom", "18", "man"]

# dict2 = {list1[k]: list2[k] for k in range(len(list1))}
dict2 = {list1[k]: list2[k] for k in range(len(list2))}
print(dict2)
# 如果两个列表长度不同，len只能统计短的列表长度，否则会报错


# 需求： 提取电脑大于等于200的
count1 = {"mac": 255, "window": 99, "lenovo": 201, "redmi": 68}

# 获取所有大于等于200的键值对
dict3 = {key: value for key, value in count1.items() if value > 200}
print(dict3)