"""Дан произвольный список, содержащий только числа. Выведите результат сложения всех чисел больше 10."""
import random

my_list = []

x = random.randint(0, 20) # kolichestvo randomnih chisel ot 0 do 20
for i in range(x):
    y= random.randint(0, 100)
    my_list.append(y )

print (my_list)
result = 0
for element in my_list:
    if element >10:
        result+=element
print (result)