from flask import Flask
from src.logger import logging

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
    logging.info("We are testing our second methods of logging")
    return "Welcome to the session of ML project"

if __name__ == "__main__":
    app.run(debug=True)