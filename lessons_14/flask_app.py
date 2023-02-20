import logging
from flask import Flask,request
from sqlalchemy import create_engine

from lessons_14.utilys import create_tables,create_user, find_user,delete_product, add_purchase,update_product
from lessons_14.models import User

from lessons.lessons_14 import utilys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def users_get():
   users = app.session.query(User).all()
   return [u.as_dict() for u in users]

@app.route("/", methods=["POST"])
def users_post():

   user = create_user(app.session, request.form.get("email"), request.form.get("password"))
   return {"user_id": user.id}


@app.route("/", methods=["POST"])
def find_some_user():
   user = find_user(app.session,"test@mail.ru")
   for data in user:
      return {data}

@app.route("/delete_product/", methods=["POST"])
def delete_product2():
    utilys.delete_product(session=app.session, product_id =int(request.form.to_dict()['id_prod']))
    return 'Product was delete'


@app.route("/add_purchase/", methods=["POST"])
def add_purchase2():
    utilys.add_purchase(session=app.session, user_id=int(request.form.to_dict()['user_id']),
                        product_id=int(request.form.to_dict()['product_id']),
                        count=int(request.form.to_dict()['count']))
    return f'Purchase added'

















if __name__ == "__main__":
   engine = create_engine("postgresql://juls:juls@localhost/juls")
   app.session = create_tables(engine)
   app.run()










# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         logger.info('Обрабатываю POST запрос')
#         for key, value in request.form.to_dict().items():
#             logger.info(f'{key}: {value}')
#         return 'hello world'
#
#     logger.info('Обрабатываю GET запрос')
#     for key, value in request.args.to_dict().items():
#         logger.info(f'{key}: {value}')
#     return 'hello world'
#
# @app.route("/", methods=["GET", "POST"])
# def abc():
#     if request.methon == 'POST':
#         logger.info('Обрабатываю POST за')