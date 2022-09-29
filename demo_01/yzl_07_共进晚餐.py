# 邀请名单
invite_list = ["tom", "bob", "alice"]

print(f"我想邀请{invite_list[0]},{invite_list[1]},{invite_list[2]}"
      f"和我一起共进晚餐".title())

print(f"突然{invite_list[0].title()}说他无法赴约")
# 修改的名单
invite_list[0] = "eric"
print(f"修改的名单为{invite_list},并向他们发出邀请".title())

# invite_lists = ["dave", "mike", "jane"]
# invite_list.extend(invite_lists)
# print(f"增加的列表为{invite_list}".title())
# 增大了餐桌后的邀请名单
print("我找到了一个更大的餐桌")
invite_list.insert(0, "dave")
invite_list.insert(2, "mike")
invite_list.append("jane")
print(f"现在我邀请了{invite_list}来跟我共进晚餐".title())

# 缩减名单
print(len(invite_list))
print("由于餐桌无法送到，现在只能邀请两位一起进餐")
sorry_list = invite_list.pop()
print(f"不好意思，{sorry_list.title()}")
sorry_list1 = invite_list.pop()
print(f"不好意思，{sorry_list1.title()}")
sorry_list2 = invite_list.pop()
print(f"不好意思，{sorry_list2.title()}")
sorry_list3 = invite_list.pop()
print(f"不好意思，{sorry_list3.title()}")

# 最后两个人依然被邀请
print(f"亲爱的{invite_list[0]},{invite_list[1]}，你们还是和我一起共进晚餐".title())

# 删除最后两个人，并打印确认
del invite_list[0]
del invite_list[0]
print(invite_list)

