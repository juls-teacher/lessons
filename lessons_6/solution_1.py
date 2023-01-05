"""Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное,
в идеале не использовать библиотечные функции."""

text =  input ("Введите текст через пробел  : ")
my_spis = (text.split())
"""
def max_leng (my_spis):
    max = len(my_spis[0])
    for element in  my_spis:
        if len(element) > max:
            max = element
    return max
print("самое длинное: ", max_leng(my_spis))"""

print("Самое длинное слово", max(my_spis,key=len))

dybli= {x for x in my_spis if my_spis.count(x)>1}
print("Повторяющееся слово ", *dybli)



