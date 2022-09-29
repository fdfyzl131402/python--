def print_info(name, title="", gender=True):
    """用缺省参数判断男生还是女生

    :param title: 职位
    :param name: 姓名
    :param gender: True 男生， False 女生
    """
    gender_text = "男生"

    if not gender:
        gender_text = "女生"
    print("【%s】%s 是 %s " % (title, name, gender_text))


# 假设男生居多，则添加默认值
print_info("小明")
print_info("小梅", gender=False)