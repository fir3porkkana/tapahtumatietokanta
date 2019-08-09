from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3)])
    password = PasswordField("Password", [validators.Length(min=3)])

    class Meta:
        csrf = False

class AccountForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3)])
    username = StringField("Username", [validators.Length(min=3)])
    password = PasswordField("Password", [validators.Length(min=3)])

    class Meta:
        csrf = False