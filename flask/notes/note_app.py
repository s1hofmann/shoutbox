from flask import Flask, render_template
from flask_bootstrap import Bootstrap

__all__ = ["app"]

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def index():
    return render_template("index.html", elements=range(12))

@app.route("/hello/<string:username>")
def say_hi(username):
    return render_template("hello.html", user=username)

@app.route("/user/<string:username>")
def user(username):
    pass

@app.route("/about/")
def about():
    return render_template("about.html")
