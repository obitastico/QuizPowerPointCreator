from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    title = StringField('Frage:', validators=[DataRequired()])
    richtig = StringField('Richtige Antwort:', validators=[DataRequired()])
    falsch1 = StringField('1. Falsche Antwort:', validators=[DataRequired()])
    falsch2 = StringField('2. Falsche Antwort:', validators=[DataRequired()])
    falsch3 = StringField('3. Falsche Antwort:', validators=[DataRequired()])
    submit = SubmitField('Submit')
    finish = SubmitField('Finish')
