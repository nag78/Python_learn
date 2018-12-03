import unittest
from city_function import get_formatted_state_city

class NameCityCase(unittest.TestCase):
    """Тесты для 'city_function.py'"""
    def test_city_state(self):
        """Тест на данные 'Santiago, Chilie.'"""
        formatted_city = get_formatted_state_city('chile','santiago')
        self.assertEqual(formatted_city, 'Santiago, Chile.')
    def test_city_state_population(self):
        """ Тест на данные с популяцией"""
        formatted_city = get_formatted_state_city('chile','santiago', '5000000')
        self.assertEqual(formatted_city, 'Santiago, Chile - population 5000000.')

unittest.main()