"""Ввести с клавиатуры строку, проверить является ли строка палиндромом и вывести результат (yes/no) на экран.
Палиндром - это слово или фраза, которые одинаково читаются слева направо и справа налево"""

str=input("vvedite stroky\n")
rev_str = ''.join(reversed(str))
if (str==rev_str):
    print (" yes  ")
else:
    print("no")