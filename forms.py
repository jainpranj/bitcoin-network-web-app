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


class RegressionForm(Form):
  grade = StringField('Grade', validators=[DataRequired("Please enter a grade")])
  total_pymnt_inv = StringField('Total Payment Inv', validators=[DataRequired("Total Payment Inv")])
  revol_util = StringField('Rovloving Utilization', validators=[DataRequired("Please enter a Rovloving Utilization")])
  loan_status = StringField('Loan Status', validators=[DataRequired("Please enter a Loan Status")])
  fico_range_grade = StringField('Fico Range Grade', validators=[DataRequired("Please enter Fico Range Grade")])
  total_rec_prncp = StringField('Ttotal Rec PRNCP', validators=[DataRequired("Please enter a Ttotal Rec PRNCP")])
  revol_bal = StringField('Revolivng Balance', validators=[DataRequired("Please enter a Revolivng Balance")])
  grade_based_on_inq_last_6mths = StringField('Grade based on Ing last 6 months', validators=[DataRequired("Please enter a Grade based on Ing last 6 months")])
  acc_open_past_24mths = StringField('Acc Open Past 24 months', validators=[DataRequired("Please enter a Acc Open Past 24 months")])
  installment = StringField('Installment', validators=[DataRequired("Installment")])
  last_pymnt_amnt = StringField('Last Payment Amount', validators=[DataRequired("Last Payment Amount")])
  funded_amnt_inv = StringField('Funder Amount Inv', validators=[DataRequired("Funder Amount Inv")])
  total_acc = StringField('Total Acc', validators=[DataRequired("Total Acc")])
  credit_age = StringField('Credit Age', validators=[DataRequired("Credit Age")])
  issue_d = StringField('Issue Date', validators=[DataRequired("Issue Date")])
  annual_inc = StringField('Annual Inc', validators=[DataRequired("Please enter a Annual Inc")])
  meanfico = StringField('Mean FICO', validators=[DataRequired("Please enter a Mean FICO")])
  cluster = StringField('cluster', validators=[DataRequired("Please enter a cluster")])

  
  submit = SubmitField("Get Rate Of Interest")



