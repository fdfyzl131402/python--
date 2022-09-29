def count_animals(filename):
    """判断异常"""
    try:
        with open(filename) as f:
            contents = f.read()

    except FileNotFoundError:
        # print(f"没找到文本{filename}")
        pass

    else:
        print(contents)
        print(f"找到了{filename}")


filenames = ["cats", "ggg", "dogs"]
for file in filenames:
    # 如果此处不使用 for  则 下面 调用函数 会报错，
    # 因为 无法把整个列表作为实参
    count_animals(filenames)

