import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
from lessons_12.models import Base, User ,Profile, Address, Product, Purchase

DB_USER = "juls"
DB_PASSWORD = "juls"
DB_NAME = "juls"
DB_ECHO = True

if __name__ == "__main__":
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}", echo=True,)
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
        session.commit()

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

        address = Address(city='Minsk', address='ul. Sovetskaya 23', user_id=user.id)
        session.add(address)
        address = Address(city='Brest', address='ul. Pervomayskaya 14', user_id=user.id)
        session.add(address)
        address = Address(city='Minsk', address='ul. Minskaya 4', user_id=user.id)
        session.add(address)
        address = Address(city='Mogilev', address='ul. Gurskogo 7 ', user_id=user.id)
        session.add(address)
        address = Address(city='Gomel', address='ul. Svobody 2', user_id=user.id)
        session.add(address)
        session.commit()


#Создать функции для добавления нового и обновления существующего адреса пользователя.
    def update_address():
        address = Address(city='New York', address='test', user_id=user.id)
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


    def create_user():
        user = User(email=input('Введите электронную почту '), password=input('Введите пароль '))
        session.add(user)
        session.commit()

        address = Address(user_id=user.id, city=input('Введите город '), address=input('Введите адрес '))
        session.add(address)

        profile = Profile(user_id=user.id, phone=input('Введите номер телефона '), age=input('Введите возраст '))
        session.add(profile)

        session.commit()


    def update_address2():
        session.query(User).filter(User.email == input('Введите почту ')).first()
        address = session.query(Address).filter(Address.address == input('Введите старый адрес ')).first()
        address.address = input('Введите новый адрес ')
        session.add(address)
        session.commit()


    def add_address():
        address = Address(user_id=input('Введите ID '), city=input('Введите город '), address=input('Введите адрес '))
        session.add(address)
        session.commit()


    def find_user():
        result = session.query(Profile).filter(Profile.age == int(input('Введите возраст пользователя ')))
        for user in result:
            logger.info(user)


    def create_product():
        product = Product(name=input('Введите название продукта '), price=float(input('Введите цену ')),
                        count=int(input('Введите количество ')), comment=input('Введите комментарий '))
        session.add(product)
        session.commit()

    def read_product():
        result = session.query(Product).filter(Product.name == input('Введите название продукта '))
        for product in result:
            logger.info(product)


    def update_product():
        product = session.query(Product).filter(Product.id == int(input('Введите ID '))).first()
        product.name = input('Введите название продукта ')
        product.price = float(input('Введите цену '))
        product.count = int(input('Введите количество '))
        product.comment = input('Введите комментарий ')
        session.add(product)
        session.commit()


    def delete_product():
        product = session.query(Product).filter(Product.id == int(input('Введите ID '))).first()
        session.delete(product)
        session.commit()





    # add_user()
    # update_address()
    # search_age()
    #
    # create_user()
    # update_address2()
    # add_address()
    # find_user()
    #
    create_product()
    # read_product()
    # update_product()
    # delete_product()
    # buy_product()





    # user = User(email="test@test.com", password="password")
    # session.add(user)
    #
    # session.commit()
    #
    # address = Address(user_id=user.id, city="Minsk", address="Test")
    # session.add(address)
    #
    # profile = Profile(user_id=user.id, phone="+375292999999", age=20)
    # session.add(profile)
    #
    # user = session.query(User).filter(User.email == "test@test.com").first()
    # user.password = "new_password"
    # session.add(user)
    # session.commit()
    #
    # result = session.query(Profile).filter(Profile.age >= 15)
    # for x in result:
    #     print(x)
    #     print(x.user)
    #

