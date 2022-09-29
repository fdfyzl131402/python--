filename = "guest.txt"

# 指定用户输入名字
# with open(filename, "w") as input_name:
with open(filename, "a") as input_name:
    while True:
        names = input("请输入你的名字：")
        # 做一个判断 ，何时退出
        if names == "q":
            break

        # 打印一条问候语
        print(f"你好，{names}")

        input_name.write(f"{names} \n")
