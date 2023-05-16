from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class CalculatorForm(FlaskForm):
      name = SelectField('Jak masz na imię?', validators=[DataRequired()])
      submit = SubmitField('Wyślij')