import os

old_file_name = input("请输入你要拷贝的文件名：")

if os.path.isfile(old_file_name):
    names = os.path.splitext(old_file_name)
    new_file_name = names[0] + ".bak" + names[1]

    old_file = open(old_file_name, "rb")  # 以二进制的形式读
    new_file = open(new_file_name, "wb")  # 同时以二进制的形式写
    new_file.write(old_file.read())

    new_file.close()
    old_file.close()
