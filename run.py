import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    """Main page with instruction"""
    return "To send a message use /USRENAME/MESSAGE"

@app.route("/<username>")
def user(username):
    return "Hi " + username


@app.route("/<username>/<message>")
def send_message(username, message):
    return "{0}: {1}".format(username, message)
    
if __name__ == '__main__':
    app.run(host="localhost", port="5000", debug=True)