students = [
    {"name": "沸羊羊"},
    {"name": "美羊羊"}
]
# 在学员中寻找美羊羊
find_name = "zhangsan"
for stu_dict in students:
    print(stu_dict)

    if stu_dict["name"] == find_name:
        print(f"找到了{find_name}")
        # 如果找到了对象就退出循环
        break
else:
    # 如果没有找到想要找的find_name，则会输出提示信息
    print(f"抱歉，没有找到{find_name}")
print("循环结束")
