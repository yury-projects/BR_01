from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, TextField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo

from app.modules.constants import Constants


class UserCreateForm(Form):
    # TODO: Validators for email
    email = TextField("Username", validators=[DataRequired(), Length(min=7, max=120)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=3, max=120), EqualTo("confirm", message="Passwords must match")])
    confirm = PasswordField("Repeat Password", validators=[DataRequired(), Length(min=3, max=120)])
    first_name = TextField("First Name", validators=[DataRequired(), Length(min=2, max=120)])
    last_name = TextField("Last Name", validators=[DataRequired(), Length(min=2, max=120)])
    org_id = SelectField("Organization", coerce=int, validators=[DataRequired()])
    role = SelectField("Role", coerce=int, choices=[(Constants.USER_ROLE_ADMIN, "Admin"), (Constants.USER_ROLE_USER, "User")], validators=[DataRequired()])
