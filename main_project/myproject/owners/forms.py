from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,IntegerField


class AddOwnerForm(FlaskForm):
    name = StringField('Name of the owner')
    puppy_id = IntegerField('ID of puppy')
    submit = SubmitField('Add owner')