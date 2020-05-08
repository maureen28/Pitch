from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    category = SelectField('Categories', choices=[('Pickup', 'Pickup Pitch'), ('Fashion', 'Fashion Pitch'), ('Business', 'Business Pitch'), ('Interview', 'Interview Pitch')], validators=[DataRequired()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave Your Comment Here')
    submit = SubmitField('Submit')