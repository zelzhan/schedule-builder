from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField

class Button(FlaskForm):
	link = SubmitField()