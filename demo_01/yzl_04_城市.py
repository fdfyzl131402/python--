def city_country(city, country):
    """返回城市对"""
    name = city
    country_name = country

    return name + country_name


result = city_country("wuhan", " chinese")
print(result)
result = city_country("new york", " American")
print(result)
result = city_country("London", " England")
print(result)
