import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello there!</h1>"


if __name__ == '__main__':
    app.run(host="localhost", port="5000", debug=True)