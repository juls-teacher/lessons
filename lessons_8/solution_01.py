"""Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0). Методы: увеличить скорости (скорость +5),
 уменьшение скорости (скорость -5), стоп (сброс скорости на 0), отображение скорости, задний ход (изменение знака скорости)."""

class Car():
    model = None
    speed = None
    year = None
    brand = None

    def __init__(self,model, year,brand,speed=0):
        self.model,self.year, self.brand, self.speed = model,year,brand , speed

    def high_speed(self):
        self.speed = self.speed + 5


    def less_speed(self):
        self.speed = self.speed - 5


    def stop_speed(self):
        self.speed = 0


    def show_speed(self):
        print(f'скорость: {self.speed}')

    def reverse_speed(self):
        self.speed = -1 * self.speed



