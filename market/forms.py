from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Username already exists! Please try using a different username")

    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError("Email already exists! Please try using a different email")

    username = StringField(label="Username:", validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label="Email:", validators=[Length(max=50), Email(), DataRequired()])
    password = PasswordField(label="Password:", validators=[Length(min=6), DataRequired()])
    confirm_password = PasswordField(label="Confirm Password:", validators=[EqualTo("password"), DataRequired()])
    submit = SubmitField(label="Create Account")

class LoginForm(FlaskForm):
    username = StringField(label="Username:", validators=[DataRequired()])
    password = PasswordField(label="Password:", validators=[DataRequired()])
    submit = SubmitField(label="Sign In")

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label="Purchase Item")

class SellItemForm(FlaskForm):
    submit = SubmitField(label="Sell Item")
