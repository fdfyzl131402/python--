while True:
    try:
        first = int(input("第一个数:"))
        second = int(input("第二个数字："))
    except ValueError:
        print("请输入一个正确的的数字")
    else:
        result = first + second
        print(result)
        if result >= 10:
            break


