from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required,Email
from ..models import User,Comment,Pitch

class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators=[Required()])
    category = SelectField('Category', choices=[('Elevator','Elevator'),('Interview','Interview'),('Product','Product'), ('Pickupline', 'Pickupline')],validators=[Required()])
    post = TextAreaField('Your Pitch', validators=[Required()])
    submit = SubmitField('Add pitch')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit') 


class CommentForm(FlaskForm):
    comment=TextAreaField('Pitch comment.',validators = [Required()])
    submit = SubmitField('Submit')
