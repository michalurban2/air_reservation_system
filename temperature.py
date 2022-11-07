from decimal import Decimal


class Temperature:
    def __init__(self, temperature):
        self._temperature = temperature  # dane do naszej klasy
        # ^ TO MA BYC PROTECTED

    @property  # tworzy cos w postaci gettera
    def temperature(self):  # interfejs
        return f'{self._temperature} °C'  # getter zawsze musi miec return

    @temperature.setter  # nazywa się tak samo, jak getter, NIE DA SIĘ STWORZYĆ GETTER BEZ SETTER
    def temperature(self, value):  # interfejs
        if not isinstance(value, (int, float, Decimal)):
            raise TypeError(f'Invalid tyle: {type(value).__name__}')

        # setter zawsze musi miec wartość i nie ma return
        if value < -273.15:
            raise ValueError(f'too low: {value}')
        self._temperature = value

    @property
    def temperature_f(self):
        return f'{self._temperature * 9 / 5 + 32} °F'  # wywołuje getter

    @temperature_f.setter
    def temperature_f(self, value):
        self.temperature = (value - 32) * (5 / 9)

    @property
    def temperature_k(self):
        return f'{self._temperature + 237.15} °K'

    @temperature_k.setter
    def temperature_k(self, value):
        self.temperature = (value - 237.15)


t = Temperature(-50)
print(t.temperature)
t.temperature = -273.15
# t.temperature = -65432
t.temperature_f = 0
t.temperature_k = 66
print(t.temperature)
print(t.temperature_f)
print(t.temperature_k)
# print(vars(t))
# print(dir(t))
# print(t.__dict__)


# print(t.get_temperature())
# t.set_temperature(42)
# t.temperature = 42
# print(t.temperature)
