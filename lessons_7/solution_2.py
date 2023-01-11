"""Дан список стран и городов каждой страны, где ключи это названия стран, а значения - списки городов в этих странах.
Написать функцию которая осуществляет поиск по городу и возвращает страну. Оформить в виде программы, которая считывает
 название города и выводит на печать страну."""

import csv

with open("city.csv", "r") as file:
   reader = csv.reader(file)
   dictionary={
       row[0]:row[2]
       for row in reader
   }


def city_to_country(word):
    return dictionary.get(word, "ERROR")


def country_to_city(word):
    return {
        value:key
        for key ,value in dictionary.items()
    }.get(word, "ERROR")

def country_to_city_2(word):
    for country,city in dictionary.items():
        if city == word:
            return country

a=input ("введите город : ")
print(country_to_city_2(a))