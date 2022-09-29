i = 1
while i <= 5:
    # 如果使用 break和continue
    if i == 3:
        print("这遍不真诚")
        # break
        i += 1  # 如果这里不计数 则会陷入死循环
        continue
    print("媳妇我错了")
    i += 1
else:
    print("媳妇原谅我了")

# 注意： for...else 和他的原理完全一样
