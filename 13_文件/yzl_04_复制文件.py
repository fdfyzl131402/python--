# 1.打开
file_read = open("README")
file_write = open("README[附件]", "w")

# 2.读、写
txt = file_read.read()
file_write.write(txt)

# 3.关闭
file_read.close()
file_write.close()