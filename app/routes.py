from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = dict(username="Felix")
    posts = [
        {
        "author": {"username": "Ted"},
        "body": "it takes all kinds of critters"
        },
        {
        "author": {"username": "Bob"},
        "body": "Hello my name is Bob."
        },
    ]
    return render_template("index.html", title="Home of the MicroBlog", user=user, posts=posts)
