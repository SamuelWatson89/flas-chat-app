import os
from datetime import datetime
from flask import Flask, redirect, render_template

app = Flask(__name__)
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


@app.route('/')
def index():
    """
    Main page with Intructions
    """
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
