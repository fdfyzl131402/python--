hello_str = "hello world"

# 判断是否以指定字符串开始
print(hello_str.startswith("hello"))
# 判断是否以指定字符串结束
print(hello_str.endswith("world"))
# 查找指定字符串
print(hello_str.find("llo"))
# 不存在,则返回-1
print(hello_str.find("abc"))
# 替换字符串
# replace 执行时会返回一个新的字符串，
# 注意：不会修改原有的字符串
print(hello_str.replace("world", "python"))
print(hello_str)
