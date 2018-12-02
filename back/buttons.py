from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField

class Button(FlaskForm):

	link = SubmitField('Add Course')
	data1 = StringField()
	data2 = StringField()