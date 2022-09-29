# 用嵌套输出九九乘法表
row = 1
# 开始循环
while row <= 9:

    col = 1

    while col <= row:
        # \t 制表符，协助在输出文本时，垂直方向保持对齐

        print("%d * %d = %d" % (col, row, col * row), end="\t")

        col += 1

    print("")

    row += 1
