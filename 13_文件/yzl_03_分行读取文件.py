file = open("README")

while True:
    # 读取一行内容
    txt = file.readline()

    # 判断是否读取到文件
    if not txt:
        break

    print(txt.rstrip())  # .rstrip() 删除字符串末尾的空白

file.close()