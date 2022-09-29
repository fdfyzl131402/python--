try:
    # 提示用户输入一个整数
    num = int(input("请输入一个整数:"))
    # 使用数字8除以用户输入的数字并输出
    result = 8 / num

    print(result)
except ZeroDivisionError:
    print("除0错误")

except ValueError:
    print("请输入正确的整数")
