# 定义变量name，输出 我的名字叫什么，请多多关照
name = "大小明"

print("我的名字叫%s，请多多关照" % name)

# 定义整数变量student_no,输出 我的学号是00001
student_no = 1
print("我的学号是%06d" % student_no)

# 定义小数变量price weight money ，输出 苹果的单价9.00/斤，重量5.00元/斤和总金额45.00元

price = 9
weight = 5
money = price * weight
print("苹果的单价为%.2f元/斤，重量为%.2f斤和总金额%.2f元" % (price, weight, money))

# 定义一个小数scale ，输出 数据比例是10%
scale = 0.25
print("数据比例是%.2f%%" % (scale * 40))