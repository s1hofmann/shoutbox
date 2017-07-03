from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from .forms import ShoutForm

__all__ = ["app"]

app = Flask(__name__)
app.config["SECRET_KEY"] = "Don't tell anyone!"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shoutbox.db"
db = SQLAlchemy(app)
Bootstrap(app)

from . import models


@app.route("/")
def index():
    shouts = models.Shout.query.all()
    return render_template("index.html", elements=shouts)

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
        name = sf.name.data
        text = sf.shout.data
        new_shout = models.Shout(name=name, text=text)
        db.session.add(new_shout)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("shout.html", form=sf)

@app.route("/about/")
def about():
    return render_template("about.html")
