"""
把字符串s中的每个空格替换成"%20"
输入:S = "We are happy."
输出:"We%20are%20happy."
"""
S = "We are happy."
print(S.replace(" ", "%20"))

# 只替换一个
print(S.replace(" ", "%20", 1))
