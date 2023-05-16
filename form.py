from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class CalculatorForm(FlaskForm):
      name = SelectField(, validators=[DataRequired()])
      submit = SubmitField('Wyślij')