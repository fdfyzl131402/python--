# 导包
import random
# 1.从控制台输出要出的拳，石头（1），剪刀（2），布（3）
player = int(input("请输入你要出的拳，石头（1），剪刀（2），布（3）:"))

# 2.电脑随机出 --先假定电脑会出石头，完成编码过程
computer = random.randint(1, 3)
print("玩家选择的是%d - 电脑出的是拳是%d" % (player, computer))

# 3.比较胜负
# 石头 胜 剪刀
# 剪刀 胜 布
# 布 胜 石头
# if (()
#       or ()
#       or ()):
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("电脑弱爆了，你大胜")

# 4.平局
elif player == computer:
    print("平局")

# 5.其他状况
else:
    print("电脑获胜")
