import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    # index page with instructions
    return "To send a message, use /USERNAME/MESSAGE"

@app.route("/<username>")
def user(username):
    return "Hi <b>" + username.capitalize()

@app.route("/<username>/<message>")
def send_message(username, message):
    return "{0}: {1}".format(username.capitalize(), message.upper())

app.run(host=os.getenv("IP"),
        port=os.getenv("PORT"),
        debug=True)