import conversions
import unittest


class TestConverterBadInput(unittest.TestCase):
    def test_convertCelsiusToKelvinvalueisfloat(self):
        """convertCelsiusToKelvin should fails if the input is not float value."""
        self.assertRaises(conversions.NotFloat, conversions.convertCelsiusToKelvin, 200)

    def test_convertCelsiusToFahrenheitvalueisfloat(self):
        """convertCelsiusToKelvin should fails if the input is not float value."""
        self.assertRaises(conversions.NotFloat, conversions.convertCelsiusToFahrenheit, 200)

class TestConverter(unittest.TestCase):
    def test_convertCelsiusToKelvin(self):
        """convertCelsiusToKelvin should return the correct output."""
        self.assertEqual(conversions.convertCelsiusToKelvin(700.00),973.15)
        self.assertEqual(conversions.convertCelsiusToKelvin(500.00), 773.15)
        self.assertEqual(conversions.convertCelsiusToKelvin(0.00), 273.15)
        self.assertEqual(conversions.convertCelsiusToKelvin(-125.25), 147.90)
        self.assertEqual(conversions.convertCelsiusToKelvin(-273.00), 0.15)

    def test_convertCelsiusToFahrenheit(self):
        """convertCelsiusToFahrenheit should return the correct output."""
        self.assertEqual(conversions.convertCelsiusToFahrenheit(100.00), 212.00)
        self.assertEqual(conversions.convertCelsiusToFahrenheit(37.00), 98.6)
        self.assertEqual(conversions.convertCelsiusToFahrenheit(0.00), 32.00)
        self.assertEqual(conversions.convertCelsiusToFahrenheit(-40.00),-40.00)
        self.assertEqual(conversions.convertCelsiusToFahrenheit(-273.15), -459.67)

if __name__ == '__main__':
    unittest.main()
