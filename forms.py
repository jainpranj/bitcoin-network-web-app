from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
  first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
  last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, message="Passwords must be 6 characters or more.")])
  submit = SubmitField('Sign up')

class LoginForm(Form):
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
  submit = SubmitField("Sign in")

class AddressForm(Form):
  address = StringField('Address', validators=[DataRequired("Please enter an address.")])
  submit = SubmitField("Search")


class ClassifcationForm(Form):
  amount_requested = StringField('Loan Amount', validators=[DataRequired("Please enter your loan amount.")])
  zip_code = StringField('Zip Code', validators=[DataRequired("Please enter a zip code.")])
  employment_length = StringField('Employment Length', validators=[DataRequired("Please enter a employment length")])
  risk_score = StringField('Risk Score', validators=[DataRequired("Please enter a credit score")])
  debt_to_income_ratio = StringField('Debt to Income Ratio', validators=[DataRequired("Please enter a credit score")])
  
  submit = SubmitField("Check loan eligibilty")