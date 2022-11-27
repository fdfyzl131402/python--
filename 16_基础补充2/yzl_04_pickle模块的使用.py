# python里存入数据只支持存入字符串和二进制
# json:将乎python里的数据(str/List/tuple/dict/int/float/bool/None)等转换成为对应的
# pickle:将Python里任意的对象转换成为二进制

import pickle

# 序列化 dumps  将python数据转化为二进制
# dump 将python数据转化为二进制，同时保存到指定的文件中
# 反序列化 loads  将二进制文件加载为python数据
# load  读取文件 ，并将文件的二进制转化为对象
names = ["张三", "李四", "王五", "jack"]
b_name = pickle.dumps(names)
# print(b_name)
file = open("name.txt", "wb")
file.write(b_name)
file.close()

file1 = open("name.txt", "rb")
x = file1.read()
y = pickle.loads(x)
print(y)
file1.close()


class Dog(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def eat(self):
        print(f"{self.name}正在吃屎")


d = Dog("大黄", "黑色")
file3 = open("dog.txt", "wb")
pickle.dump(d, file3)
file3.close()

file4 = open("dog.txt", "rb")
dd = pickle.load(file4)
print(dd)
dd.eat()
print(dd.name, dd.color)
