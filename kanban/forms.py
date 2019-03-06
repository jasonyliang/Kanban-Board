from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.fields.html5 import DateField


class ToDoForm(FlaskForm):
	title = StringField('Title', validators=[
                           DataRequired(), Length(min=2, max=50)])
	description = TextAreaField('Description', validators=[DataRequired()])
	deadline = DateField('Deadline', format='%Y-%m-%d', validators=[DataRequired()])
	submit = SubmitField('Post')