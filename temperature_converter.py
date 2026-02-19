class TemperatureConverter:

    def celsius_to_fahrenheit(self, c):
        return c * 9 / 5 + 32

    def fahrenheit_to_celsius(self, f):
        return (f - 32) * 5 / 9

    def celsius_to_kelvin(self, c):
        if c < -273.15:
            raise ValueError("Температура ниже абсолютного нуля недопустима")
        return c + 273.15

    def kelvin_to_celsius(self, k):
        if k < 0:
            raise ValueError("Температура по Кельвину не может быть отрицательной")
        return k - 273.15

    def is_below_freezing(self, c):
        return c < 0
