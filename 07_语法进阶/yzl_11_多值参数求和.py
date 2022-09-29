def sum_numbers(*args):

    num = 0
    print(args)
    # 循环遍历元组求和
    for n in args:
        num += n
        # num = num + n
    return num


result = sum_numbers(1, 2, 3, 4, 5)
print(result)