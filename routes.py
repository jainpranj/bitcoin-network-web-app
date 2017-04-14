from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User, Place, Classifcation
from forms import SignupForm, LoginForm, AddressForm,ClassifcationForm
import urllib2
import json


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
db.init_app(app)

app.secret_key = "development-key"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/success")
def success():
  return render_template("success.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
  if 'email' in session:
    return redirect(url_for('home'))

  form = SignupForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()

      session['email'] = newuser.email
      return redirect(url_for('home'))

  elif request.method == "GET":
    return render_template('signup.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
  if 'email' in session:
    return redirect(url_for('home'))

  form = LoginForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template("login.html", form=form)
    else:
      email = form.email.data 
      password = form.password.data 

      user = User.query.filter_by(email=email).first()
      if user is not None and user.check_password(password):
        session['email'] = form.email.data 
        return redirect(url_for('home'))
      else:
        return redirect(url_for('login'))

  elif request.method == 'GET':
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
  session.pop('email', None)
  return redirect(url_for('index'))


@app.route("/classification",methods=["GET", "POST"])
def classification():


  form = ClassifcationForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template("classification.html", form=form)
    else:

      amount_requested = form.amount_requested.data 
      risk_score = form.risk_score.data
      debt_to_income_ratio = form.debt_to_income_ratio.data
      zip_code = form.zip_code.data
      employment_length = form.employment_length.data


      data = {
          "Inputs": {
                  "input1":
                  [
                      {
                              'Amount_Requested': amount_requested,   
                              'Loan_Title': "1",   
                              'Risk_Score': risk_score,   
                              'Debt-To-Income_Ratio': "10",   
                              'Zip_Code': zip_code,   
                              'Employment_Length': employment_length,   
                              'Policy_Code': "1",   
                              'accept_reject_loan': "1",   
                              'State': "1",   
                      }
                  ],
          },
      "GlobalParameters":  {
      }
      }

      body = str.encode(json.dumps(data))

      url = 'https://ussouthcentral.services.azureml.net/workspaces/f28500a2409240e0912181212c9e7c5e/services/9aab259ced0b46dc96788ef0708269be/execute?api-version=2.0&format=swagger'
      api_key = 'yLH77qMmvFBxsqnSP37eIOEvk4wcV1CedkbwZOcptB92eOu48Gu6IQ9Hi7AQsurxpI82Qk+W+O89+sMyj1pvfw=='
      headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

      req = urllib2.Request(url, body, headers)

      try:
        response = urllib2.urlopen(req)

        result = response.read()
        resp_dict = json.loads(result)
        print(result)
        loaneligibilty=resp_dict['Results']['output1'][0]['Scored Labels']
        
        print(loaneligibilty)
        c= Classifcation()
        print(c)
        status=c.get_status(loaneligibilty)
      except urllib2.HTTPError, error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read()))
      #return  redirect(url_for('success'))
      return render_template('success.html',status=status)


  elif request.method == 'GET':
    return render_template('classification.html', form=form)


@app.route("/home", methods=["GET", "POST"])
def home():
  if 'email' not in session:
    return redirect(url_for('login'))

  form = AddressForm()

  places = []
  my_coordinates = (53.2734, -7.778320310000026)

  if request.method == 'POST':
    if form.validate() == False:
      return render_template('home.html', form=form)
    else:
      # get the address
      address = form.address.data 

      # query for places around it
      p = Place()
      my_coordinates = p.address_to_latlng(address)
      places = p.query(address)

      # return those results
      return render_template('home.html', form=form, my_coordinates=my_coordinates, places=places)

  elif request.method == 'GET':
    return render_template("home.html", form=form, my_coordinates=my_coordinates, places=places)

if __name__ == "__main__":
  app.run(debug=True)