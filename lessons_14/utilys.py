from sqlalchemy.orm import sessionmaker

from lessons_13.models2 import Base
from lessons_13.models2 import User, Product, Purchase,Profile


def create_tables(engine):
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


def create_user(session, email, password):
    user = User(email=email, password=password)
    session.add(user)
    session.commit()
    return user

def find_user(session, ids: int):
    query = session.query(User).filter_by(id=ids).first()
    return query.id, query.email

def create_product(session, name, price, count, comment):
    product = Product(name=name, price=price, count=count, comment=comment)
    session.add(product)
    session.commit()
    return product


def find_user(session, email):
    return session.query(User).filter(User.email == email).first()

def add_purchase(session, user_id, product_id,count):
    purchase = Purchase(user_id=user_id, product_id = product_id, count=count)
    session.add(purchase)
    session.commit()
    return purchase


def delete_product(session, product_id):
    session.query(Product).filter_by(id=product_id).delete()
    session.commit()

def update_product(session,product_id, name, price,count, comment):
     session.query(Product).filter_by(id=product_id).update({"name": f"{name}", "price": f"{price}","count": f"{count}", "comment": f"{comment}"})
     session.commit()


def search_purchases_by_user(session, email): # doesnt work
    user_id = session.query(User.id).filter(User.email == email)
    purchase = session.query(Purchase).filter(Purchase.user_id == user_id).all()
    return purchase




def search_product_by_user(session,product_id): # Добавить функцию вывода всех пользователей, которые покупали определенный товар. (many to many)
    purchases = session.query(Purchase).filter_by(product_id=product_id)
    user_ids = []
    for purchase in purchases:
        user_ids.addend(purchase.user_id)
    return list(set(purchase.user_ids))

def get_users(session):
    users= session.querty(User).all()
    return [u.as_dict() for u in users]

