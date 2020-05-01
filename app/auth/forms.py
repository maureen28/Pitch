from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, Submitfield
from wtforms.validators import Required, Email, EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    username = StringField('Enter your username', validators=[Required()])
    password = PasswordField('password', validators=[Required(), EqualTo('password_confirm', message = 'Passwords must match')])
    password_confirm = PasswordField('password', validators=[Required()])
    submit = Submitfield('Sign up')
    
class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    password = PasswordField('password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = Submitfield('Log in')