# 需求：有两个变量比较大小，如果变量1大于变量2,则执行变量1 - 变量2 ，
# 反之则执行变量2 - 变量1
aa = 10
bb = 6
cc = aa-bb if aa > bb else bb - aa
print(cc)