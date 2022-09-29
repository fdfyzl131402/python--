class Cat:

    def eat(self):
        # 那一个对象调用的方法，self就是那一个对象的引用
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 爱喝水" % self.name)


# 创建猫对象
tom = Cat()
# 可使用. 属性名  给对象增加属性
tom.name = "Tom"
tom.eat()
tom.drink()

print(tom)
addr = id(tom)
print("%d" % addr)
# 再创建一个猫对象
lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)
lazy_cat2 = lazy_cat
print(lazy_cat2)