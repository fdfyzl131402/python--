poem_str = "\t静夜思\t李白\t床前明月光\n意识地上霜\t巨头王明月\t低头思故乡"

print(poem_str)
# 拆分字符串
poem_list = poem_str.split()
print(poem_list)
# 合併字符串
result = " ".join(poem_list)
print(result)