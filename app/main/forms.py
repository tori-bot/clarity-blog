e
from typing import Optional
from unicodedata import category
from flask_wtf import FlaskForm
from ..models import Blog 
from wtforms import StringField,SubmitField,SelectField,TextAreaField
from wtforms.validators import DataRequired,Optional
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Update ')

class UpdateAdminProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Update ')

class CommentForm(FlaskForm):
    comment=TextAreaField('Leave a comment',validators=[DataRequired()])
    submit=SubmitField('Submit')

class BlogForm(FlaskForm):
    title= StringField('Blog title',validators=[DataRequired()] )
    category=SelectField('Which category',choices=[('technology','technology'),('politics','politics'),('entertainment','entertainment '),('personal','personal ')],validators=[Optional()])
    content=TextAreaField('Get creative',validators=[DataRequired()])
    submit=SubmitField('Submit')

class SubscribeForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired()])
    name=StringField('Name',validators=[DataRequired()])
    submit=SubmitField('Submit')