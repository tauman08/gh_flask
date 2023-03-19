from wtforms import  StringField, validators, TextAreaField,  SubmitField, SelectMultipleField
from flask_wtf import FlaskForm   

class CreateArticleForm(FlaskForm):
    title = StringField("Title",[validators.DataRequired()])
    text = TextAreaField("Text",[validators.DataRequired()])
    tags = SelectMultipleField('Tags',coerce=int)
    submit = SubmitField('Create')

