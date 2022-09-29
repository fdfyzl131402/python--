# 1.定义布尔变量has_ticket，通过代码检查是否有票
has_ticket = True

# 2.定义整数变量knife_length,表示刀的长度，单位：cm
knife_length = 30

# 3.首先检查是否有票，有才能进入
if has_ticket:
    print("可以进入")

# 4.检查刀的长度是否超过20cm，未超过提示可以入内
    if knife_length <= 20:
        print("请进入车站")

# 5.刀的长度超过则不能进入
    else:
        print("您携带的刀有 %d cm，违反规定，不得入内" % knife_length)

# 6.如果没票也不能入内
else:
    print("不能进入")
    



