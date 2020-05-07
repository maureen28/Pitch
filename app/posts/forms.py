from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from app.models import User

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    category = SelectField('Categories', choices=[('Fashion Pitch', 'Fashion Pitch'), ('Pickup Pitch ', 'Pickup Pitch'), ('Business Pitch', 'Business Pitch'), ('Promotion Pitch', 'Interview Pitch')], validators=[DataRequired()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment Here')
    submit = SubmitField('Submit')