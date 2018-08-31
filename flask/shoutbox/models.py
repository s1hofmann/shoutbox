from .shoutbox_app import db


class Shout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    text = db.Column(db.Text)

    def __init__(self, name, text):
        self.username = name
        self.text = text
