from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     length(min=8,
                                                            max=64,
                                                            message='Password has length between 8 and 64 characters')])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')


