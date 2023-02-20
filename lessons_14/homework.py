# import logging
# from flask import Flask, request
# from sqlalchemy import create_engine
# from sqlalchemy_utils import create_database, database_exists
# import utilys
#
# app = Flask(__name__)
#
# logging.basicConfig(level=logging.INFO)
# loger = logging.getLogger(__name__)
#
# DB_USER = "juls"
# DB_PASSWORD = "juls"
# DB_NAME = "juls"
#
#
# if __name__ == "__main__":
#     engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}")
#     if not database_exists(engine.url):
#         create_database(engine.url)
#
#     session = utilys.create_tables(engine)
#
#
# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "GET":
#         for ids in request.args.to_dict().items():
#             response = utilys.find_user(session=session,ids=ids)
#             loger.info(f'{response}')
#     elif request.method == "POST":
#         utilys.create_user(session=session,
#                           email=request.form.to_dict()['email'],
#                           password=request.form.to_dict()['password'])
#     return 'запись существует '
#
#
# if __name__ == "__main__":
#     app.run()

from flask import Flask

from sqlalchemy import create_engine

from lessons_14.utilys import create_tables
from lessons_14.models import User

app = Flask(__name__)  # объект класса фласк

DB_USER = "juls"
DB_PASSWORD = "juls"
DB_NAME = "juls"


@app.route("/", methods=["GET"])
def index():
   users = app.session.query(User).all()
   return [u.as_dict() for u in users]


if __name__ == "__main__":
   engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}')
   app.session = create_tables(engine)
   app.run()
