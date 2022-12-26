"""Пользователь вводит с клавиатуры числа до тех пор, пока не введет любой строчный символ, из этих чисел составляется первый список.
Далее таким же образом вводятся второй и третий списки. Вывести на экран список, элементы которого есть в первых двух списках, но отсутствуют в третьем."""
my_dict={0:[],1:[],2:[]}

for index, lst  in my_dict.items():
    while True:
        current_symbol = input()
        if current_symbol.isnumeric():  # входная строка 123 1 вернет труе, диджит фолс труе
            lst.append(current_symbol)
        else:
            break

all_elements=my_dict[0]+my_dict[1]+my_dict[2]
new_list=[]
for element in all_elements:
    #элементы которого есть в первых двух списках, но отсутствуют в третьем
    if element in my_dict[0] and element in my_dict[1] and element in my_dict[2]:
        new_list.append(element)

print(new_list)
