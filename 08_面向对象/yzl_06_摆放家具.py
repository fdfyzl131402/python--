class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 % .2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具名称列表
        self.item_list = []

    def __str__(self):
        # python 可以自动将一对小括号内部的代码连在一起
        return ("户型： %s\n总面积： %.2f  剩余面积： [%.2f]\n家具： %s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加的家具 %s" % item)
        # 1.判断家具的面积，如果超过了房子面积就提示不能塞进去
        if item.area > self.free_area:
            print("%s的面积太大，无法放进房子" % item.name)
            return
        # 2. 将家具的名词添加到列表中
        self.item_list.append(item.name)
        # 3.计算剩余面积
        self.free_area -= item.area


# 1.创建家具对象
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

print(bed)
print(chest)
print(table)

# 2.创建房子对象
my_house = House("两室一厅", 60)
my_house.add_item(bed)
my_house.add_item(chest)
my_house.add_item(table)
print(my_house)