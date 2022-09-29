# 不到三岁的观众收费3元，三到十二岁的观众收费10元，超过12岁的观众收费15元。循环实现

prompt = "请输入您的年龄 ："

while True:
    age = input(prompt)
    if age == "quit":
        break
    else:
        age = int(age)
        if age < 3:
            print("free")
        elif 3 <= age <= 12:
            print("您的票价是10元")
        else:
            print("您的票价是15元")
        # prompt = "\nPlease enter the your age:"
        # prompt += "\n(Enter 'quit' when you are finished.) "
        #
        # while True:
        #     age = input(prompt)
        #     if age == 'quit':
        #         break
        #     else:
        #         age = int(age)
        #         if age < 3:
        #             print("free")
        #         elif (age >= 3 and age <= 12):
        #             print("The ticket price is 10 dollars.")
        #         else:
        #             print("The ticket price is 15 dollars.")

