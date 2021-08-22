from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required,Email
from ..models import User,Comment,Pitch

class PitchForm(FlaskForm):
    title = StringField('Pitch Category', validators=[Required()])
    pitch = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Add pitch')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit') 


class CommentForm(FlaskForm):
    comment=TextAreaField('Pitch comment.',validators = [Required()])
    submit = SubmitField('Submit')
