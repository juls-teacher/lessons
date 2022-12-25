"""Получить сумму кубов натуральных чисел от n до m используя цикл for, числа n и m вводятся с клавиатуры."""

n= int(input("vvedi nachalnoe chislo"))
m= int(input ("vvedi poslednee chislo "))
sum = 0
for i in range(n,m):
    sum+=i**3
print (sum)