strs = "hello world and hello python and yzl"
# 1. .find()
print(strs.find("and"))
print(strs.find("and", 15, 45))
print(strs.find("andd"))

# 2. .index()
print(strs.index("and"))
print(strs.index("and", 15, 45))
# print(str.index("andd"))  报错

# 3. .count()
print(strs.count("and"))
print(strs.count("and", 15, 45))
print(strs.count("andd"))

# 4.replace()
new_strs = strs.replace("and", "he")
print(strs)
print(new_strs)
# 字符串是不可变类型，所以replace有返回值，
# 只是把返回值修改了，同时如果替换次数超过已有的字符串，只会替换现有的所有字符串
new_str = strs.replace("hello", "hei", 5)
print(new_str)

# 5.split(), 分割，返回一个列表， 会丢失分割字符
list1 = strs.split("and")
print(list1)
list2 = strs.split("and", 1)
print(list2)

# 6..join()
list = ["aa", "bb", "cc"]

# aa...bb...cc
new_list = '...'.join(list)
print(new_list)

# .capitalize（） 字符串第一个字母转化为大写
# .title () 字符串每个单词的第一个字母都大写
# .lower() 把字符串每个字母都小写
# .upper（）把字符串每个字母都大写
