"""Создать программу позволяющую осуществлять поиск по имени или возрасту, оба параметра вводятся с клавиатуры."""

from classwork11_01 import select_user
from classwork11_01 import select_user_age

print(f"""Программа  осуществляет  поиск по имени или возрасту".\n Поиск по имени: name. \n Поиск по возрасту: age .""")
choice = int(input(f"Введите параметр поиска name (1) или age (2) : "))
while choice != 1  and choice != 2:
    choice = int(input(f"Неверный ввод параметра , введите цифру: "))
if choice == 1:
    print(select_user(input(f"Введите имя для поиска : ")))
elif choice == 2:
    print(select_user_age(input(f"Введите min возраст от :   "), (input(f"Введите max возраст  до:   "))))




