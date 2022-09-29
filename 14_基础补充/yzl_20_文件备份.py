# 1. 用户输入目标文件
old_name = input("请输入要备份的文件名：")
# print(old_name)

# 2. 规范备份的文件名
# 名字和后缀分离  -- 找到最右侧的点才是后缀的格式
# 要判断文件名有没有前缀，如果没有则无法运行

index = old_name.rfind(".")
if index > 0:
    postfix = old_name[index:]
# print(index)
# 提取原名字
# print(old_name[:index])
# print(old_name[index:])
# new_name = old_name[:index] + '【备份】' + old_name[index:]
new_name = old_name[:index] + "【备份】" + postfix
print(new_name)

# 3. 备份文件写入内容
# 打开 源文件  和 备份文件
old_f = open(old_name, "rb")
new_f = open(new_name, "wb")
# 读取源文件 ， 写入备份文件
while True:
    con = old_f.readline()
    if not con:
        break
    new_f.write(con)

# 关闭文件
old_f.close()
new_f.close()