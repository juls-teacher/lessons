"""Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца - и возвращает название сезона, к которому
 относится этот месяц. Например, передаем 2, на выходе получаем "Winter"."""
my_map = {
    "Winter":[12,1,2],
    "Sping":[3,4,5],
    "Summer":[6,7,8],
    "Autumn":[9,10,11]
}

def month_to_season(month_number):
    for season,months in my_map.items():
        if month_number in months:
            return season



print(month_to_season(2))