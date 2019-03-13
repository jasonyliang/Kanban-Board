from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.fields.html5 import DateField
from kanban.models import User

class ToDoForm(FlaskForm):
	title = StringField('Title', validators=[
                           DataRequired(), Length(min=2, max=50)])
	description = TextAreaField('Description', validators=[DataRequired()])
	deadline = DateField('Deadline', format='%Y-%m-%d', validators=[DataRequired()])
	submit = SubmitField('Post')


# User forms
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    passwordConfirm = PasswordField('Confirm Password',
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    # Template:
    # def validate_field(self, field):
    #     if True:
    #         raise ValidationError('Validation Message')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken, please choose another one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is used, please choose another one.') 


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


