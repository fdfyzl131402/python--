info_tuple = ("小明", 18, 1.75)

# 格式字符串后面的（）本质上是元组
print("%s  年龄是%d  身高是%.2f" % info_tuple)

info_str = "%s  年龄是%d  身高是%.2f" % info_tuple
print(info_str)