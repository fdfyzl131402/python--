# test_cities.py
import unittest
from city_functions import get_city_country


class TestCase(unittest.TestCase):
    """测试city函数"""
    def test_city_functions(self):
        cities_functions = get_city_country("santiago", "chile")
        self.assertEqual(cities_functions, "Santiago From Chile")

    def test_city_country_population(self):
        city_country_population = get_city_country("santiago", "chile", "50000000")
        self.assertEqual(city_country_population, "Santiago From Chile-population=50000000")


if __name__ == '__main__':
    unittest.main()
