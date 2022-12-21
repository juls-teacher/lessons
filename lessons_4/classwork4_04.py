"""Написать программу, которая будет выводить на экран случайные числа от 1 до 10 до тех пор, пока не выпадет 7."""
from  random import randint


while True:
    x = randint(0, 10)
    if x==7:
         break
    print (x)


#VTOROI VARIANT RESHENIA
x=0
while x!=7:
    x = randint(0, 10)
    print(x)
