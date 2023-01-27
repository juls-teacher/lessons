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



#if __name__== "main":
create_product("Phone",1200,12,"mobile phone")
create_product("Washmachine", 450,10, "None")