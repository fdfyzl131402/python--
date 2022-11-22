"""
1.己知一个字符串为"hello_world_yoyo",如何得到一个队列["hello", "world", "yoyo"]

2.让用户输入任意的用户名与密码，然后将他输入的用户名与密码打印出来，如用户输入abc/123，则打印
您输入的用户名是:abc
密码是:123
"""
a = "hello_world_yoyo"
print(a.split("_"))

b = input("请输入您的用户名和密码：(user/passwd)")
c = b.split("/")
print("您输入的用户名是:%s" % c[0])
print("密码是:%s " % c[1])
