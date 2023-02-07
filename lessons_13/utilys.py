from sqlalchemy.orm import sessionmaker

from lessons_13.models2 import Base
from lessons_13.models2 import User

def create_tables(engine):
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

def create_user(session, email, password):
    user = User(email=email, password=password)
    session.add(user)
    session.commit()
    return user

def find_user(session,email):
    return session.query(User).filter(User.email == email).first()


