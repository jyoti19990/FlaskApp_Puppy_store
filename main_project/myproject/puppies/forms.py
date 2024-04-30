from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,IntegerField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    name = StringField('Name of the puppy')
    submit = SubmitField('Add puppy')
class DelForm(FlaskForm):
    id = IntegerField('ID number to be deleted')
    submit = SubmitField('Remove puppy')