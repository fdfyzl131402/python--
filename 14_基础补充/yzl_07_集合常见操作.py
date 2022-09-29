# 1.增加数据 add()  update()    集合是可变类型  并且有去重功能
s1 = {10, 20, 30}
s1.add(10)
print(s1)

# s1.add([10, 20])  # 报错
# print(s1)

s1.update([10, 20, 30, 40])
print(s1)

# s1.update(10)  # 报错
# print(s1)

# 2.删除数据  remove(） discard()  pop()
# remove()   删除指定数据，如果数据不存在则会报错
s2 = {10, 20, 30, 40, 50}
s2.remove(10)
print(s2)

# s2.remove(10) # 报错
# print(s2)

# discard（） 删除指定数据，如果不存在不会报错
# s2.discard(10)
# print(s2)

s2.discard(10)  # 不报错，且会重新打印一次
print(s2)

# pop()  随机删除某个数据,并且返回这个数据（同时只有字符串类型才会随机删除）
s3 = set("abcdefg")
del_num = s3.pop()
print(del_num)
print(s3)
s2.pop()
print(s2)

# 3.查找数据  in  或者  not in  判断
print(10 in s2)
print(10 not in s2)