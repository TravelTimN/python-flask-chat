import os
from datetime import datetime
from flask import Flask, redirect

app = Flask(__name__)
messages = []

def add_messages(username, message):
    # assign current time into 'now' variable
    now = datetime.now().strftime("%H:%M:%S")
    # add messages to the 'messages' list above
    messages.append("[@{0}] {1}: {2}".format(now, username, message))

def get_all_messages():
    # get all of the messages and separate using <br>
    return "<br>".join(messages)

@app.route("/")
def index():
    # index page with instructions
    return "To send a message, use /USERNAME/MESSAGE"

@app.route("/<username>")
def user(username):
    # display welcome to user
    return "<h1>Welcome, <b>{0}</b>!</h1> {1}".format(username.capitalize(), get_all_messages())

@app.route("/<username>/<message>")
def send_message(username, message):
    # create a new message and redirect back to the chat page
    add_messages(username.capitalize(), message.upper())
    return redirect(username)

app.run(host=os.getenv("IP"),
        port=os.getenv("PORT"),
        debug=True)