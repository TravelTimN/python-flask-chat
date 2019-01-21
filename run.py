import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "randomstring123")
messages = []

def add_message(username, message):
        # assign current time (now) into 'now' variable
        now = datetime.now().strftime("%H:%M:%S")
        # add time/user/message into dictionary
        #messages_dict = {"timestamp": now, "from": username, "message": message}
        # add messages to the 'messages' list above
        #messages.append("[{0}] {1}: {2}".format(now, username, message))
        #messages.append(messages_dict)
        messages.append({"timestamp": now, "from": username, "message": message})

""" # commenting out since this is now being worked in the dictionary above
def get_all_messages():
        # get all of the messages and separate using <br>
        return "<br>".join(messages)
"""

@app.route("/", methods=["GET", "POST"])
def index():
        if request.method == "POST":
                session["username"] = request.form["username"]
        
        if "username" in session:
                #return redirect(session["username"])
                return redirect(url_for("user", username = session["username"]))
        
        # index page with instructions
        # return "To send a message, use /USERNAME/MESSAGE"
        return render_template("index.html")

@app.route("/chat/<username>", methods = ["GET", "POST"])
def user(username):
        # add and display chat messages
        if request.method == "POST":
                username = session["username"]
                message = request.form["message"]
                add_message(username, message)
                #return redirect(session["username"])
                return redirect(url_for("user", username = session["username"]))

        return render_template("chat.html", username = username, chat_messages = messages)
        # display welcome to user
        #return "<h1>Welcome, <b>{0}</b>!</h1> {1}".format(username.capitalize(), messages)
        # get_all_messages no longer in use since everything in dictionary now
        #return "<h1>Welcome, <b>{0}</b>!</h1> {1}".format(username.capitalize(), get_all_messages())

""" # not needed anymore
@app.route("/<username>/<message>")
def send_message(username, message):
        # create a new message and redirect back to the chat page
        add_message(username, message)
        #add_message(username.capitalize(), message.upper())
        return redirect(username)
"""

app.run(host=os.getenv("IP", "0.0.0.0"),
        port=os.getenv("PORT", "5000"),
        debug=False)