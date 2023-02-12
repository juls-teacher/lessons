
import logging
from flask import Flask, request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        logger.info ("обрабатываем POST запрос")
        return request.form.to_dict()
   #return request.args.to_dict()
    logger.info("обрабатываем GET запрос")
    for key,value in request.args.to_dict().items():
        logger.info(f"{key}= {value}")

    return "hello"


if __name__ == "__main__":
    app.run()
