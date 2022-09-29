class Person:
    def __init__(self, name, weight):
        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"我叫{self.name},我{self.weight}公斤"

    def run(self):
        print(f"{self.name}爱锻炼，锻炼可以减肥")
        self.weight -= 0.5

    def eat(self):
        print(f"{self.name}是吃货，吃完再减肥")
        self.weight += 1


xiaoming = Person("小明", 75.0)
xiaoming.run()
xiaoming.eat()
print(xiaoming)

# 小美也爱跑步
xiaomei = Person("小美", 45.0)
xiaomei.eat()
xiaomei.run()
print(xiaomei)
# 两个对象互不干扰
print(xiaoming)