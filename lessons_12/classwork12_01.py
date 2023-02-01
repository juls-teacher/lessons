from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from lessons_12.models import Base, User ,Profile, Address

DB_PATH = Path(__file__).resolve().parent / "my_database.sqlite3"
DB_ECHO = True


if __name__ == "__main__":
    engine = create_engine(f"sqlite:////{DB_PATH}", echo=DB_ECHO)
    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()


    def add_user():
        user = User(email="test@test.com", password="password")
        session.add(user)
        user = User(email="test2@test.com", password="password2")
        session.add(user)
        user = User(email="test3@test.com", password="password3")
        session.add(user)
        user = User(email="test4@test.com", password="password4")
        session.add(user)
        user = User(email="test5@test.com", password="password5")
        session.add(user)

        profile = Profile(phone='+375251111111', age='25', user_id=user.id)
        session.add(profile)
        profile = Profile(phone='+375251111112', age='26', user_id=user.id)
        session.add(profile)
        profile = Profile(phone='+375251111113', age='28', user_id=user.id)
        session.add(profile)
        profile = Profile(phone='+375251111114', age='28', user_id=user.id)
        session.add(profile)
        profile = Profile(phone='+375251111115', age='30', user_id=user.id)
        session.add(profile)

        address = Address(city='Minsk', address='ul. Sovetskaya 23', user_id=275)
        session.add(address)
        address = Address(city='Brest', address='ul. Pervomayskaya 14', user_id=276)
        session.add(address)
        address = Address(city='Minsk', address='ul. Minskaya 4', user_id=277)
        session.add(address)
        address = Address(city='Mogilev', address='ul. Gurskogo 7 ', user_id=user.id)
        session.add(address)
        address = Address(city='Gomel', address='ul. Svobody 2', user_id=user.id)
        session.add(address)
        session.commit()


#Создать функции для добавления нового и обновления существующего адреса пользователя.
    def update_address():
        address = Address(city='New York', address='test', user_id=277)
        session.add(address)
        session.commit()
        session.query(Address).filter_by(city='Gomel').update({"city": "Gomel !!!!!"})
        session.add(address)
        session.commit()

#Создать функцию для поиска всех пользователей с определенным возрастом.
    def search_age():

        profile = session.query(Profile).filter(Profile.age >= 26)
        for row in profile:
            print(f'{row.phone}.{row.age}.{row.id}')
        session.commit()




    add_user()
    update_address()
    search_age()