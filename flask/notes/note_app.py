from flask import Flask

__all__ = ['app']

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello ConSolis!</h1>"
