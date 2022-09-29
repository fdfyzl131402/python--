def make_car(build, size, **car_style):
    """用一个字典，包含汽车的一些信息

    :param build: 'subaru'
    :param size: 'outback'
    :param car_style: 'blue',True
    :return: 'car_manufacturer','car_model'
    """
    car_style["car_manufacturer"] = build
    car_style["car_model"] = size
    return car_style


car = make_car("subaru", "outback", color="blue", tow_packet="True")
print(car)

