"""Дана база данных (в виде текстового файла) о продажах некоторого интернет-магазина. Каждая строка входного файла представляет собой запись
вида Покупатель, Товар, Количество, Стоимость ,где Покупатель - имя покупателя (строка без пробелов), товар - название товара (строка
 без пробелов), количество - количество приобретенных единиц товара.
Создайте список и выведите на экран всех покупателей,  а для каждого покупателя подсчитайте общее количество приобретенных им товаров и их стоимость. """

import csv
list=[]
with open("shop.csv", "r") as file:
   reader = csv.reader(file)

   for col in reader:
       list.append(col[0])
print(" ".join(set(list)))






