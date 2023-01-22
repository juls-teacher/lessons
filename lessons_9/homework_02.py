"""Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран.
print("1-прямоугольник, 2-треугольник, 3-круг")


figure = input("Выберите фигуру: ")
if figure == '1':
    print("Длины сторон прямоугольника:")
    a = float(input("a = "))
    b = float(input("b = "))
    print("Площадь: %.2f" % (a * b))
elif figure == '2':
    print("Длины сторон треугольника:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    p = (a + b + c) / 2
    from math import sqrt
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print("Площадь: %.2f" % s)
elif figure == '3':
    r = float(input("Радиус круга R = "))
    from math import pi
    print("Площадь: %.2f" % (pi * r ** 2))
else:
    print("Ошибка ввода")"""

class Square():
   def __init__(self, length):
       self.length = length

   def area(self):
       return self.length ** 2


class Circle():
   def __init__(self, radius):
       self.radius = radius

   def area(self):
       return 3.14 * self.radius ** 2

class Triangle() :
    def __init__(self, ab,bc,ca):
        self.ab = ab
        self.bc = bc
        self.ca = ca

    def area(self):
        self.p = (self.ab + self.bc + self.ca) / 2
        return (self.p * (self.p - self.ab) * (self.p - self.bc) * (self.p - self.ca)) ** (1 / 2)


