import json

filename = "numbers.json"
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    numbers = int(input("请输入你喜欢的数字:"))
    with open(filename, "w") as f:
        json.dump(numbers, f)
        print(f"你喜欢的数字是 %s" % numbers)
else:
    print(number)




