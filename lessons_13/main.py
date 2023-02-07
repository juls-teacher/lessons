import logging

from sqlalchemy import create_engine

from sqlalchemy_utils import create_database, database_exists
from lessons_12.models import Base, User ,Profile, Address, Product, Purchase
from lessons_13.utilys import create_tables
from lessons_13.utilys import create_user

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_USER = "juls"
DB_PASSWORD = "juls"
DB_NAME = "juls"

if __name__ == "__main__":
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}")
    if not database_exists(engine.url):
        create_database(engine.url)

    session = create_tables(engine)


    menu= """
        1 .Создать пользователя
        2. Найти пользователя
        3. EXIT
        """

    while True:
        logger.info(menu)
        choice = input("выберите действие:  ")


        if choice == "1":
            email = input('Введите электронную почту ')
            password = input('Введите пароль ')
            user = create_user(session, email, password)
            logger.info(f'пользователь  #{user.id} создан')
        elif choice == "3":
            exit()

