def print_line(char, times):

    print(char * times)


def print_lines(char, times):
    """打印多行分割线

    :param char: 分割使用的分割字符
    :param times: 分隔字符的数量
    """
    row = 0
    while row < 5:

        print_line(char, times)

        row += 1


name = "yzl"
