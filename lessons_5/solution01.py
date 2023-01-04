"""Создайте функцию three_args(), которая принимает 1, 2 или 3 ключевых параметра.
В результате ее работы на печать выводятся значения переданных переменных, но только если они не равны None.
Получим, например, следующее сообщение:Переданы аргументы: var1 = 2, var3 = 10."""
"""def my_func(*args):
   for value in args:
       print(value)
my_func(5, 7, 15)

def my_func(**kwargs):
   for key, value in kwargs.items():
       print(key, value)
my_func(a=5, b=7, c=15)"""

def three_args(**kwargs):
   list=[]
   for key,value in kwargs.items():
      if value is not None:
         list.append(f"{key}={value}")
   print(*list)
three_args(var1=None,var2= None,var3=256)
