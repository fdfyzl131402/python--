"""
输入一个字符串str,输出第m个只出现过n次的字符，
如在字符串gbgkkdehh中,找出第2个只出现1次的字符，输出结果:d
解决思路:
利用collections库的 Counter方法统计字符串每个单词出现的次数
"""
from collections import Counter

a = "gbgkkdehh"
b = Counter(a)
print(dict(b))

s = []
for k, v in dict(b).items():
    print(k, v)
    if v == 1:
        s.append(k)
print(s[1])
# 列表推导式
print([k for k, v in dict(b).items() if v == 1][1])

