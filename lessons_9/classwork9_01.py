"""Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы: переопределить магические методы сравнения (==, !=, >=, <=, <, >).
Переопределить магические методы сложения, вычитания, умножения на число.
Создать метод, который выводит на экран отформатированное время (HH:MM:SS).
Создать объект класса MyTime, умножить его на 2 и вывести на печать результат.
Создать второй объект класса MyTime, найти разницу с первым, добавить к нему 7 часов и 45 минут, вывести на печать результат.
Добавить новый класс MyDateTime унаследованный от MyTime. В конструктор добавить новые атрибуты: day, month, year. “Исправить” все магические методы для этого класса.
Создать объект класса MyDateTime, умножить его на 2 и вывести на печать результат."""

from __future__ import annotations

class MyTime():
    hours = None
    minutes = None
    seconds = None

    def __init__(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds
        self.timestamp = seconds + minutes * 60 + hours * 60 * 60

    def __eq__(self, other) -> bool:
        return self.timestamp == other.timestamp
        # ( self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds)   сравнивает значения и возвращается true

    def __ge__(self, other) -> bool:
        return self.timestamp >= other.timestamp

    def __lt__(self, other) -> bool:
        return self.timestamp < other.timestamp

    def __add__(self, other) -> int:
        timestamp = self.timestamp + other.timestamp
        hours = timestamp // (60 * 60)
        minutes = (timestamp % (60 * 60)) // 60
        seconds = timestamp % 60
        return MyTime(hours, minutes, seconds)  # self.__class__ вместо   MyTime

    def __str__(self):
        return f'MyTime {self.hours}:{self.minutes}:{self.seconds}'

    def __repr__(self):
        return f'MyTime {self.hours}:{self.minutes}:{self.seconds}'

    def __mul__(self, other):
        return f'MyTime {self.hours * 2}:{self.minutes *2 }:{self.seconds *2}'

    def __sub__(self, other):
        timestamp = self.timestamp - other.timestamp
        hours = timestamp // (60 * 60)
        minutes = (timestamp % (60 * 60)) // 60
        seconds = timestamp % 60
        return MyTime(hours, minutes, seconds)

class MyDateTime(MyTime):
    day = None
    month = None
    year =None

    def __init__(self, day,month, year):
        self.day, self.month, self. year = day, month, year
        self.timestamp2 = day + month * 30 + year * 365

    def __eq__(self, other) -> bool:
        return self.timestamp2 == other.timestamp2

    def __add__(self, other) -> int:
        timestamp2 = self.timestamp2 + other.timestamp2
        day = timestamp2
        month = timestamp2 // 30
        year = timestamp2 // 365

        return MyDateTime(day,month,year)





if __name__ == "__main__":
    time1 = MyTime(12, 20, 12)
    time2 = MyTime(12, 20, 1)
    print(time1 == time2)  # магические  методы явно не вызываются  print (time1.__eq__(time2))
    print(time1 + time2)
    time_mult = MyTime(10, 23, 12) #создали новый объект класса
    print(time_mult * 2)
    time3 = MyTime(2, 45, 6)
    time4 = MyTime(7,45,0)
    print(time_mult - time3+time4)

    year1 = MyDateTime(12,2,1991)
    year2 = MyDateTime(10,6,2000)
    print(year1 == year2)
    print(year1+year2)


