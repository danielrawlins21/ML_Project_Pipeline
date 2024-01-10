from flask import Flask
from src.logger import logging
from src.exception import CustomException
import os, sys

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
    try:
        #logging.info("We are testing our second methods of logging")
        raise Exception("We are testing our custom file")
    except Exception as e:
        abc = CustomException(e, sys)
        logging.info(abc.error_message)
        return "Welcome to the session of ML project"

if __name__ == "__main__":
    app.run(debug=True)