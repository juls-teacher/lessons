"""Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure. Создать три дочерних класса Circle (атрибуты: координаты центра, длина радиуса;
методы: нахождение периметра и площади окружности), Triangle (атрибуты: три точки, методы: нахождение площади и периметра), Square (атрибуты: две точки, методы:
нахождение площади и периметра). При потребности создавать все необходимые методы не описанные в задании. """

import math

class Point() :

    def __init__ (self,x,y):
        self.x = x
        self.y = y

class Figure():
    def __init__ (self, area, perimeter):
        self.area = area
        self.perimetr = perimeter


class Circle(Figure):
    def __init__(self, x,y,radius):
        self.x = x
        self.y = y
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Figure) :

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.lenght = x2 - x1
        self.width = y2 - y1

    def side(self):
        return self.lenght, self.width

    def area(self):
        return self.lenght * self.width

    def perimeter(self):
        return 2 * (self.lenght + self.width)

class Triangle(Figure) :
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.ab = ((x2-x1)**2 +(y2-y1)**2)**(1/2)
        self.bc = ((x3-x2)**2 +(y3-y2)**2)**(1/2)
        self.ca = ((x3-x1)**2 +(y3-y1)**2)**(1/2)

    def perimeter(self):
        return self.ab+self.bc + self.ca

    def area(self):
        self.p = (self.ab + self.bc + self.ca)/2
        return  (self.p*(self.p-self.ab)*(self.p-self.bc)*(self.p-self.ca) )** (1/2)




O = Circle(0, 0, 3)  # объект класса круг
print(O.area())
print(O.perimeter())

P = Square(2,0,9,4) # объект класса прямоугольник
print(P.area())
print(P.perimeter())

T = Triangle(0,0,0,6,5,0)
print(T.area())
print(T.perimeter())













