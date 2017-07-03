from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from .forms import ShoutForm

__all__ = ["app"]

app = Flask(__name__)
app.config["SECRET_KEY"] = "Don't tell anyone!"
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

@app.route("/shout/", methods=["GET", "POST"])
def shout():
    sf = ShoutForm()
    if sf.validate_on_submit():
        name = sf.name
        text = sf.shout
        return redirect(url_for("index"))
    return render_template("shout.html", form=sf)

@app.route("/about/")
def about():
    return render_template("about.html")
