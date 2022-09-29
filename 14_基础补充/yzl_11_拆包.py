# 元组拆包
def return_num():
    return 100, 200


num1, num2 = return_num()
print(num2)
print(num1)

# 字典数据拆包
dict1 = {"name": "tom", "age": "18"}
a, b = dict1
print(a)
print(b)

# v值
print(dict1[a])
print(dict1[b])