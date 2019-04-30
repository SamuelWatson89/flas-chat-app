import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "tatallyrandom9876"
messages = []


def add_messages(username, message):
    """
    Add messages to the 'messages' list
    """
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}) {}: {}".format(now, username, message))


def get_all_messages():
    """
    Get all the message and separate using a break
    """
    return "<br>".join(messages)


@app.route('/', methods=["GET", "POST"])
def index():
    """
    Main page with Intructions
    """
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])

    return render_template("index.html")


@app.route('/<username>')
def user(username):
    """
    Display chat messages
    """
    return "<h1>Welcome, {0}</h1>  {1} ".format(username, get_all_messages())


@app.route('/<username>/<message>')
def send_message(username, message):
    """
    Create a new message and redirect to the chat page
    """
    add_messages(username, message)
    return redirect("/" + username)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
