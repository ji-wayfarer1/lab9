import unittest
from temperature_converter import TemperatureConverter

class TestTemperatureConverter(unittest.TestCase):
    def setUp(self):
        self.conv = TemperatureConverter()

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(self.conv.celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(self.conv.celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(self.conv.celsius_to_fahrenheit(-40), -40)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(self.conv.fahrenheit_to_celsius(32), 0)
        self.assertAlmostEqual(self.conv.fahrenheit_to_celsius(212), 100)
        self.assertAlmostEqual(self.conv.fahrenheit_to_celsius(-40), -40)

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(self.conv.celsius_to_kelvin(0), 273.15)
        self.assertAlmostEqual(self.conv.celsius_to_kelvin(-273.15), 0)
        with self.assertRaises(ValueError):
            self.conv.celsius_to_kelvin(-300)

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(self.conv.kelvin_to_celsius(0), -273.15)
        self.assertAlmostEqual(self.conv.kelvin_to_celsius(273.15), 0)
        with self.assertRaises(ValueError):
            self.conv.kelvin_to_celsius(-1)

    def test_is_below_freezing(self):
        self.assertTrue(self.conv.is_below_freezing(-1))
        self.assertFalse(self.conv.is_below_freezing(0))
        self.assertFalse(self.conv.is_below_freezing(10))


if __name__ == "__main__":
    unittest.main()
