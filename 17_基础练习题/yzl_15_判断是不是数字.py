"""判断一个字符串是不是纯数字组成"""
a = "123"
b = "abc"
print(int(a))
c = "123.33"  # 转换成整形

try:
    print(int(b))
except:
    print("不是纯数字")


# 判断字符串只是由数字组成
print(b.isdigit())