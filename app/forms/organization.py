from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class OrganizationCreateForm(Form):
    name = StringField("name", validators=[DataRequired(), Length(min=4, max=120)])
