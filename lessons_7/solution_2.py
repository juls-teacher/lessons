"""Дан список стран и городов каждой страны, где ключи это названия стран, а значения - списки городов в этих странах.
Написать функцию которая осуществляет поиск по городу и возвращает страну. Оформить в виде программы, которая считывает
 название города и выводит на печать страну."""

import csv

with open("city.csv", "r") as file:
   reader = csv.reader(file)
   dictionary={
       row[0]:row[1]
       for row in reader
   }


def eng_to_rus(word):
    return dictionary.get(word, "ERROR")


def rus_to_eng(word):
    return {
        value:key
        for key ,value in dictionary.items()
    }.get(word, "ERROR")

def rus_to_eng_2(word):
    for country,city in dictionary.items():
        if city == word:
            return country

a=input ("введите город : ")
print(rus_to_eng_2(a))