from flask import Flask, render_template

__all__ = ['app']

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello ConSolis!</h1>"

@app.route('/hello/<string:username>')
def user(username):
    return render_template("hello.html", user=username)
