from wtforms import  StringField, validators, PasswordField, SubmitField
from flask_wtf import FlaskForm   


class UserLoginForm(FlaskForm):
    email = StringField("E-mail",[validators.DataRequired(), validators.Email()])
    password = PasswordField("Password",[validators.DataRequired()])

    submit = SubmitField('Login')

