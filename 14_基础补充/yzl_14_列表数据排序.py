list1 = [{"name": "tom", "age": 15},
         {"name": "jack", "age": 13},
         {"name": "bin", "age": 16}]
# 按照k name进行排序
list1.sort(key=lambda x: x["name"], reverse=True)
print(list1)

# 按照 k age
list1.sort(key=lambda x: x["age"])
print(list1)

print(list1[0])