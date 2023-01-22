"""Создать программу, которая импортирует класс из предыдущей задачи, создает объект и при инициализации устанавливает марку Mercedes,
модель E500, год выпуска 2000. Далее “разгоняет” машину до 100 км/ч и выводит скорость на экран."""

from lessons_8.solution_01 import Car
import time

if __name__=="__main__":

    car = Car("E500", "2000"," Mercedes")
    while car.speed < 100:
        car.high_speed()
        time.sleep(1)
        car.show_speed()
    print(car.model,car.year,car.brand,car.speed)





