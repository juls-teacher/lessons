"""Использую функцию из предыдущей задачи, написать программу игру Блэкджек, т.е. реализовать цикл в котором на каждом ходу у
 игрока спрашивается, достать ли следующую карту, в случае положительного ответа  - вытягивать случайную карту.
 Игра заканчивается если игрок отказывается брать карту, либо сумма его карт больше 21-го."""

import random
"""
nominal =['6','7','8','9','10','J','D','K','A']
masti =['Hearts', 'Diamonds', 'Clubs', 'Spades']
print (random.choice(nominal),random.choice(masti))"""

cards =[6,7,8,9,10,2,3,4,11]*4
random.shuffle(cards)
count = 0

while True:
    choice = input('Возьмете карту ? y/n\n')
    if choice == 'y':
        nominal = cards.pop()
        print('Вам попалась карта номиналом ',nominal)
        count += nominal
        if count > 21:
            print('У вас ',count ,' очков и вы проиграли')
            break
        elif count == 21:
            print('Поздравляю, вы набрали 21!')
            break
        else:
            print('У вас',count,' очков.' )
    elif choice == 'n':
        print('У вас', count,' очков и вы закончили игру.')
        break


