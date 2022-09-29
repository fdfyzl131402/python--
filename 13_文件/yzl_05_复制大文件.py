# 1.打开
file_read = open("README")
file_write = open("README[附件]", "w")

# 2.读、写
while True:
    # 读取一行内容
    txt = file_read.readline()
    # 判断是否读取到文件
    if not txt:
        break

    file_write.write(txt)


# 3.关闭
file_read.close()
file_write.close()