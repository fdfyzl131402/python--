def sum_numbers(num):

    # 1. 出口
    if num == 1:
        return 1

    # 2.数字的累加 num +(1....num-1)
    # 假设sum_numbers 能正常处理1....num-1
    temp = sum_numbers(num - 1)
    # 两个数累加
    return num + temp


result = sum_numbers(5)
print(result)


