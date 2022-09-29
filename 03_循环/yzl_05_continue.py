i = 0

while i <= 10:

    # continue执行时，不执行后续代码
    # i == 3
    if i == 3:
        # 注意：在使用continue时，需要确认循环的计数是否更改，否则会出现死循环
        i += 1

        continue

    print(i)

    i += 1