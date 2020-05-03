from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, Submitfield
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    username = StringField('Enter your username', validators=[Required()])
    password = PasswordField('password', validators=[Required(), EqualTo('password_confirm', message = 'Passwords must match')])
    password_confirm = PasswordField('password', validators=[Required()])
    submit = Submitfield('Sign up')
    
    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')
        
    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')
    
class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    password = PasswordField('password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = Submitfield('Log in')