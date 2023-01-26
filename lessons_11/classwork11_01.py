
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

def select_user_age():

   with sqlite3.connect("my_database.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           SELECT *
           FROM user
           WHERE age BETWEEN 20 AND 30;
           """
       )
       session.commit()
       return cursor.fetchall()

if __name__== "main":
    create_user("Alexander", "Chaika", "manti.by@gmail.com", "TestPass", 36)
    create_user("Anton", "Golub", "birds@gmail.com", "TestPass", 30)
    create_user("Dima", "Ivanov", "ivanov_dima@gmail.com", "TestPass", 23)
    create_user("Ulia", "Akinfina", "bestartist@gmail.com", "TestPass", 25)
    create_user("Viktor", "Petrov", "petrov@gmail.com", "TestPass", 13)


res = select_user("Dima")
print(res)
print("-----------------------------")

result = select_user_age()

for row in result:

    print("Age: ", row)
    print("*"*40)

