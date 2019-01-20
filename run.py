import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []

def add_messages(username, message):
        # assign current time (now) into 'now' variable
        now = datetime.now().strftime("%H:%M:%S")
        # add messages to the 'messages' list above
        messages.append("[{0}] {1}: {2}".format(now, username, message))

def get_all_messages():
        # get all of the messages and separate using <br>
        return "<br>".join(messages)

@app.route("/", methods=["GET", "POST"])
def index():
        if request.method == "POST":
                session["username"] = request.form["username"]
        
        if "username" in session:
                return redirect(session["username"])
        
        # index page with instructions
        # return "To send a message, use /USERNAME/MESSAGE"
        return render_template("index.html")

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