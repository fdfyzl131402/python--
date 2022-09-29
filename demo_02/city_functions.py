# city_functions.py
def get_city_country(city, country, population=""):
    """生成城市from国家"""
    if population:
        city_country = f"{city} from {country}-population={population}"

    else:
        city_country = f"{city} from {country}"
        return city_country.title()