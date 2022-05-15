from flask_wtf import FlaskForm
from wtforms import stringField,SubmitField,PasswordField,BooleanField 
from wtforms.validators import DataRequired,EqualTo,Length
from wtforms.widgets import TestArea


# Create A Search Form
class SearchForm(FlaskForm):
    searched = stringField("Searched",validators=[DataRequired()])
    submit = SubmitField("Submit")
    
    
# Create Login Form
class LoginForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired()])
    password = PasswordField9("Password",validators=[DataRequired()])
    submit = SubmitField("Submit")
    
    
    # Create a Posts Form
    class PostForm(FlaskForm):
        title = stringField("Title",validators=[DataRequired])
        content = stringField("Content",validators)
        author = StringField("Author")
        slug = stringField("Slug",validators=[DataRequired])
        submit = SubmitField("Submit")