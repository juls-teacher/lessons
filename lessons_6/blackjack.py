
import random

cards =[6,7,8,9,10,2,3,4,11]*4

def choice():
    score=0
    while True:
        choice = input('Возьмете карту ? y/n\n')
        if choice == 'y':
            nominal = cards.pop()
            print('Вам попалась карта номиналом ', nominal)
            score += nominal
            if score > 21:
                print('У вас ', score, ' очков и вы проиграли')
                break
            elif score == 21:
                print('Поздравляю, вы набрали 21!')
                break
            else:
                print('У вас', score, ' очков.')
        elif choice == 'n':
            print('У вас', score, ' очков и вы закончили игру.')
            break

choice()