"""Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий. Реализовать
следующие функции для продуктов: создание, чтение, обновление по id, удаление по id. """

import sqlite3

def create_product(name: str, price: int, number:int, comment:str):
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

def show_products():
    with    sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
           """
          SELECT *
          FROM shop;
          """
        )
    session.commit()
    return cursor.fetchall()



def delete_product_by_id():
    id_input = int(input('Введите id записи для удаления: '))
    with    sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(" DELETE FROM shop  WHERE id =? ; ", (id_input,))
    session.commit()
    return cursor.fetchall()


#if __name__== "main":
create_product("Phone",1200,12,"Philips")
create_product("Wash machine", 450,10, "Bosch")
create_product("refrigerator", 1100,35, "Samsung")
create_product("coffee machine", 120,80, "Tassimo ")

all = show_products()
print('\n'.join(map(str,all)))

del_pr = delete_product_by_id()
print(del_pr)


