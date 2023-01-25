"""Установить библиотеку sqlite3 в операционную систему.
Используя консоль, создать базу sqlite3, в ней создать таблицу пользователей, добавить новую запись, прочитать её и удалить. Подключить базу в PyCharm.
Создать python функцию, которая создает таблицу user, для примера использовать слайд №12. Запустить функцию и проверить, что создался файл базы данных.
Создать функцию, которая позволяет добавлять данные в таблицу user. Добавить 5 различных записей.
Создать функцию для поиска всех пользователей с определенным именем. Запустить функцию и найти хотя бы одного пользователя по имени.
Создать функцию для поиска всех пользователей в возрасте от X до Y лет."""


import sqlite3

def create_user(firstname: str, lastname: str, email: str, password: str, age: int):
   with sqlite3.connect("my_database.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           INSERT INTO user (firstname, lastname, email, password, age)
           VALUES (?, ?, ?, ?, ?);
           """,
           (firstname, lastname, email, password, age),
       )
       session.commit()

def select_user(firstname: str):
   with sqlite3.connect("my_database.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           SELECT *
           FROM user
           WHERE firstname = ?;
           """,
           (firstname,)
       )
       session.commit()
       return cursor.fetchone()

def select_user_age(age:int):

   with sqlite3.connect("my_database.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           SELECT *
           FROM user
           WHERE ((age> 20) = ? , (age <30 )=  ?);
           """,
           (age,)
       )
       session.commit()
       return cursor.fetchone()

if __name__ == "__main__":
    create_user("Alexander", "Chaika", "manti.by@gmail.com", "TestPass", 36)
    create_user("Anton", "Golub", "birds@gmail.com", "TestPass", 30)
    create_user("Dima", "Ivanov", "ivanov_dima@gmail.com", "TestPass", 23)
    create_user("Ulia", "Akinfina", "bestartist@gmail.com", "TestPass", 25)
    create_user("Viktor", "Petrov", "petrov@gmail.com", "TestPass", 13)





result = select_user("Dima")
print(result)
print("-----------------------------")
result_age = select_user_age()
print(result_age)

