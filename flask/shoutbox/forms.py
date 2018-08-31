from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ShoutForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    shout = TextAreaField('Shout:', validators=[DataRequired()])
    submit = SubmitField('Submit')