
import sqlite3

from homework1 import show_products
from homework1 import update_product
from homework1 import delete_product_by_id


def create_product():
    print('Введите данные ')
    name = input('Название продукта: ')
    price = int(input('Цена: '))
    number = int(input('Количество: '))
    comment = input('Комментарий: ')
    with sqlite3.connect("products.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           INSERT INTO shop (name,price,number,comment)
           VALUES (?, ?, ?, ?);
           """,
           (name,price,number,comment),
       )
       session.commit()


def choose_fun():
    print('''
1 - Добавить новую запись
2 - Вывести все записи
3 - Обновить значение 
4 - Удалить значение
    ''')
    n = input('Введите номер функции: ')
    if n == '1':
        create_product()
    elif n == '2':
        show_products()
    elif n == '3':
        update_product()
    elif n == '4':
        delete_product_by_id()
    else:
        print(f'Неверно введена функция')
        choose_fun()
choose_fun()