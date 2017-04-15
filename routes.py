from flask import Flask, render_template, request, session, redirect, url_for

from models import db, User, Place, Classifcation
from forms import SignupForm, LoginForm, AddressForm,ClassifcationForm,RegressionForm

import urllib2
import json


from models import db, User, Place
from forms import SignupForm, LoginForm, AddressForm



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'


db.init_app(app)

app.secret_key = "development-key"

@app.route("/")
def index():
  return render_template("index.html")


@app.route("/regression", methods=["GET", "POST"])
def regression():
  
  return render_template("regression.html")

@app.route("/success", methods=["GET", "POST"])
def success():

  form=RegressionForm()
  if request.method == "POST":
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      grade = form.grade.data 
      total_pymnt_inv = form.total_pymnt_inv.data
      revol_util = form.revol_util.data
      loan_status = form.loan_status.data
      fico_range_grade = form.fico_range_grade.data

      total_rec_prncp = form.total_rec_prncp.data 
      revol_bal = form.revol_bal.data
      grade_based_on_inq_last_6mths = form.grade_based_on_inq_last_6mths.data
      acc_open_past_24mths = form.acc_open_past_24mths.data
      installment = form.installment.data

      last_pymnt_amnt = form.last_pymnt_amnt.data 
      funded_amnt_inv = form.funded_amnt_inv.data
      total_acc = form.total_acc.data
      credit_age = form.credit_age.data
      issue_d = form.issue_d.data
      annual_inc = form.annual_inc.data
      meanfico = form.meanfico.data
      cluster = form.cluster.data

      data = {
              "Inputs": {
                      "input1":
                      [
                          {
                                  'acc_open_past_24mths': acc_open_past_24mths,   
                                  'addr_state': "GA",   
                                  'annual_inc': annual_inc,   
                                  'chargeoff_within_12_mths': "0",   
                                  'collection_recovery_fee': "1.12",   
                                  'collections_12_mths_ex_med': "0",   
                                  'credit_age': credit_age,   
                                  'delinq_2yrs': "0",   
                                  'delinq_amnt': "0",   
                                  'dti': "1",   
                                  'earliest_cr_line_year': "1999",   
                                  'emp_length': "1",   
                                  'emp_title': "Ryder",   
                                  'fico_range_grade': fico_range_grade,   
                                  'funded_amnt_inv': funded_amnt_inv,   
                                  'grade': grade,   
                                  'grade_based_on_inq_last_6mths': grade_based_on_inq_last_6mths,   
                                  'home_ownership': "RENT",   
                                  'initial_list_status': "f",   
                                  'installment': installment,   
                                  'int_rate': "15.27",   
                                  'issue_d': issue_d,   
                                  'last_pymnt_amnt': last_pymnt_amnt,   
                                  'loan_amnt': "2500",   
                                  'loan_status': loan_status,   
                                  'meanfico': meanfico,   
                                  'mo_sin_old_il_acct': "127",   
                                  'mo_sin_rcnt_tl': "8",   
                                  'mort_acc': "1",   
                                  'mths_since_last_delinq': "0",   
                                  'mths_since_last_record': "0",   
                                  'num_accts_ever_120_pd': "0",   
                                  'num_actv_rev_tl': "5",   
                                  'num_tl_op_past_12m': "2",   
                                  'open_acc': "3",   
                                  'out_prncp': "0",   
                                  'out_prncp_inv': "0",   
                                  'pct_tl_nvr_dlq': "94.07",   
                                  'percent_bc_gt_75': "47.46",   
                                  'pub_rec': "0",   
                                  'pub_rec_bankruptcies': "0",   
                                  'purpose': "car",   
                                  'recoveries': "122.9",   
                                  'revol_bal': revol_bal,   
                                  'revol_util': revol_util,   
                                  'term': "60",   
                                  'total_acc': total_acc,   
                                  'total_pymnt_inv': total_pymnt_inv,   
                                  'total_rec_int': "435.17",   
                                  'total_rec_prncp': total_rec_prncp,   
                                  'verification_status': "Source Verified",   
                          }
                      ],
              },
          "GlobalParameters":  {
          }
      }
      data1 = {
              "Inputs": {
                      "input1":
                      [
                          {
                                  'acc_open_past_24mths': acc_open_past_24mths,   
                                  'addr_state': "GA",   
                                  'annual_inc': annual_inc,   
                                  'chargeoff_within_12_mths': "0",   
                                  'collection_recovery_fee': "1.12",   
                                  'collections_12_mths_ex_med': "0",   
                                  'credit_age': credit_age,   
                                  'delinq_2yrs': "0",   
                                  'delinq_amnt': "0",   
                                  'dti': "1",   
                                  'earliest_cr_line_year': "1999",   
                                  'emp_length': "1",   
                                  'emp_title': "Ryder",   
                                  'fico_range_grade': fico_range_grade,   
                                  'funded_amnt_inv': funded_amnt_inv,   
                                  'grade': grade,   
                                  'grade_based_on_inq_last_6mths': grade_based_on_inq_last_6mths,   
                                  'home_ownership': "RENT",   
                                  'initial_list_status': "f",   
                                  'installment': installment,   
                                  'int_rate': "15.27",   
                                  'issue_d': issue_d,   
                                  'last_pymnt_amnt': last_pymnt_amnt,   
                                  'loan_amnt': "2500",   
                                  'loan_status': loan_status,   
                                  'meanfico': meanfico,   
                                  'mo_sin_old_il_acct': "127",   
                                  'mo_sin_rcnt_tl': "8",   
                                  'mort_acc': "1",   
                                  'mths_since_last_delinq': "0",   
                                  'mths_since_last_record': "0",   
                                  'num_accts_ever_120_pd': "0",   
                                  'num_actv_rev_tl': "5",   
                                  'num_tl_op_past_12m': "2",   
                                  'open_acc': "3",   
                                  'out_prncp': "0",   
                                  'out_prncp_inv': "0",   
                                  'pct_tl_nvr_dlq': "94.07",   
                                  'percent_bc_gt_75': "47.46",   
                                  'pub_rec': "0",   
                                  'pub_rec_bankruptcies': "0",   
                                  'purpose': "car",   
                                  'recoveries': "122.9",   
                                  'revol_bal': revol_bal,   
                                  'revol_util': revol_util,   
                                  'term': "60",   
                                  'total_acc': total_acc,   
                                  'total_pymnt_inv': total_pymnt_inv,   
                                  'total_rec_int': "435.17",   
                                  'total_rec_prncp': total_rec_prncp,   
                                  'verification_status': "Source Verified",
                                  'kmean.label':cluster  
                          }
                      ],
              },
          "GlobalParameters":  {
          }
      }

      body = str.encode(json.dumps(data))
      #first service
      url1 = 'https://ussouthcentral.services.azureml.net/workspaces/f28500a2409240e0912181212c9e7c5e/services/0d389db6f8754b0c897424a5541e6a42/execute?api-version=2.0&format=swagger'
      api_key1 = 'aADBmnJDKBYQoFahbG8ltpXlE1GNox7pHrF9XFGwq5eFTCx2532rw3rkeC++7rYyWyWcUTjFJ5i2vfxdncu/fA=='
      headers1= {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key1)}

      req1 = urllib2.Request(url1, body, headers1)

      #kmeans neural network
           
      # url2 = 'https://ussouthcentral.services.azureml.net/workspaces/f28500a2409240e0912181212c9e7c5e/services/9af35ab5b80f4fe992a1c5c37b00ac09/execute?api-version=2.0&format=swagger'
      # api_key2 = 'UrXwVITTK8BIPK+MdXd3bwaFDRrzF5g0/bd7niyhUUHR0Sn/VmH8K22zqOZmA+d55hG+BKOAJK9OprToViAKDA=='
      # headers2= {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key2)}

      # req2 = urllib2.Request(url2, body, headers2)

      #grade based clustering
      if grade=='A':
        urlA = 'https://ussouthcentral.services.azureml.net/workspaces/cf9db2d296c44cc48f8ac7c8ae841965/services/699b1833b85c4b94a008a688ec835e41/execute?api-version=2.0&format=swagger'
        api_keyA = 'UGjGYwFZKsNAW27bdgSCl2liFKHOXqptYALC1UUhFlSLFruMBHDdG3mwjpfPEjbJc+BaSXxuaYjYLSzqenR2/A=='
        headersA= {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_keyA)}

        reqA = urllib2.Request(urlA, body, headersA)
      elif grade=='B':
        urlA = 'https://ussouthcentral.services.azureml.net/workspaces/cf9db2d296c44cc48f8ac7c8ae841965/services/d2bd910538a040d7a8457f6009056485/execute?api-version=2.0&format=swagger'
        api_keyA = 'VyWNtV5Am4ETDXn8m7vLosGg7MbdsNr+fa+bUdaETmhSWSeE3nr18V1Kr4aundEIxjyhDa9/Z7e/LePNbsJrmA=='
        headersA= {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_keyA)}

        reqA = urllib2.Request(urlA, body, headersA)
      elif grade=='C':
        urlA = 'https://ussouthcentral.services.azureml.net/workspaces/cf9db2d296c44cc48f8ac7c8ae841965/services/0e4fc6a9623348148893b6f6b0b578e7/execute?api-version=2.0&format=swagger'
        api_keyA = 'kRcp2GNdtYDVBG+8oEuHscdkEGqlMmpIyn51n2599qclx5xRNuxtwwdLtEXXGJMhZYlVMEXtAl5itsnDldIrzA=='
        headersA= {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_keyA)}
        reqA = urllib2.Request(urlA, body, headersA)

      elif grade=='D':
        urlA = 'https://ussouthcentral.services.azureml.net/workspaces/cf9db2d296c44cc48f8ac7c8ae841965/services/d079df7639df48d18a975e84c6ba5dba/execute?api-version=2.0&format=swagger'
        api_keyA = 'gNdclVCTZZ5iV8MJTfZ4jg1WbKI84WANnQ4QODaRomsaXanTbf+i7fYy38G3LPUu68xJdM3u2/nyL/y6cCgvjg=='
        headersA= {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_keyA)}

        reqA = urllib2.Request(urlA, body, headersA)

      elif grade=='E':
        urlA = 'https://ussouthcentral.services.azureml.net/workspaces/f28500a2409240e0912181212c9e7c5e/services/bdfb218806eb47c995632f17a3854c19/execute?api-version=2.0&format=swagger'
        api_keyA = 'MyOB6sgpIpAk9PLCrYCN4pb6EghlkdUutH9OpuglvU6nbtqABKRZCSkZZqGzXh0TcVTpXHkUnSxbiMZccfKRQw=='
        headersA= {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_keyA)}

        reqA = urllib2.Request(urlA, body, headersA)

      elif grade=='F':
        urlA = 'https://ussouthcentral.services.azureml.net/workspaces/cf9db2d296c44cc48f8ac7c8ae841965/services/ba7dde61ecbe4fb3b9ef47fb26208b83/execute?api-version=2.0&format=swagger'
        api_keyA = 'HjPYwJZX/PuplU1vmcYLse/xqxInTN5T8f8TftaOO2MPuqX3URusAOOrZ3GFbs0QsxuwkL8jZK7DPG0qeP5R5w=='
        headersA= {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_keyA)}

        reqA = urllib2.Request(urlA, body, headersA)

      elif grade=='G':


        urlA = 'https://ussouthcentral.services.azureml.net/workspaces/f28500a2409240e0912181212c9e7c5e/services/279f0282fc7e4568bff168610c46a3d2/execute?api-version=2.0&format=swagger'
        api_keyA = 'gOk0OUlqxTyXfuC25d01YhHWp3dHn5stHXWhp1ASOm/eH2EZvHOCOJ7KylWgDdOkzEpBA1vSBu0aItQkNFHJww=='
        headersA= {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_keyA)}

        reqA = urllib2.Request(urlA, body, headersA)

        #kmeans clustering
      body1 = str.encode(json.dumps(data1))
      if cluster=='0':
        urlK = 'https://ussouthcentral.services.azureml.net/workspaces/f28500a2409240e0912181212c9e7c5e/services/edf40bd621ee492d956c4b4059e927e3/execute?api-version=2.0&format=swagger'
        api_keyK = 'm9bC7BWYM/xXaGAYfNLv+gRf8WfHaB+pCXudum3ZbjQNB4HeZ/9vdXBAJS49EfrlUzuEId077kezBe333ZkJ4Q=='
        headersK= {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_keyK)}

        reqK= urllib2.Request(urlK, body1, headersK)
      elif cluster=='1':
        urlK = 'https://ussouthcentral.services.azureml.net/workspaces/f28500a2409240e0912181212c9e7c5e/services/e859dffd77e24b9a9ebb0914f144dff7/execute?api-version=2.0&format=swagger'
        api_keyK = 'lxlWNGMpmiuWASZQSaZJgq7luZTPE4U69whMd/y+lJYQP7TXUM6JAvqJjsbabl5VmNKqH+pzjpiQY5NnHGNKQw=='
        headersK= {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_keyK)}

        reqK= urllib2.Request(urlK, body1, headersK)

        
      elif cluster=='2':
        urlK = 'https://ussouthcentral.services.azureml.net/workspaces/f28500a2409240e0912181212c9e7c5e/services/339196b609344ed7812b086dcbf2585f/execute?api-version=2.0&format=swagger'
        api_keyK = 'TNCvF69yHRY3xAwhja5FoXABcchKdOq+rqK64OAUMtWkP+yMDc5IzR1jIEiCIUmkiTdo+olo4qcLGBOdIohiIw=='
        headersK= {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_keyK)}

        reqK= urllib2.Request(urlK, body1, headersK)

      elif cluster=='3':
        urlK = 'https://ussouthcentral.services.azureml.net/workspaces/f28500a2409240e0912181212c9e7c5e/services/bb61ad240f0f4be5aec6cfc7d11dcf20/execute?api-version=2.0&format=swagger'
        api_keyK = '0WaEZgNQXJisb9WV7pbHOs2JQfCfgmiE2GnSZwVEaUzfUPNRK55YPsMfH1bYnVJGTUVqJ2oaMzLSn/eI8VEz/Q=='
        headersK= {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_keyK)}

        reqK= urllib2.Request(urlK, body1, headersK)

      elif cluster=='4':
        urlK = 'https://ussouthcentral.services.azureml.net/workspaces/f28500a2409240e0912181212c9e7c5e/services/edae7e6de58a4a828689404fd8a9cf9d/execute?api-version=2.0&format=swagger'
        api_keyK = 'O2RqimXS4qD6NokOfKXlyHeTamzkeLtUAq6L4jfgOV/noOLNMlWUNfsqtJBFhAgEejViVX8rczVw7Fg8JeBhCw=='
        headersK= {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_keyK)}

        reqK= urllib2.Request(urlK, body1, headersK)

      elif cluster=='5':
        urlK = 'https://ussouthcentral.services.azureml.net/workspaces/f28500a2409240e0912181212c9e7c5e/services/194155dbb21e4546aabdf12e70d5a03a/execute?api-version=2.0&format=swagger'
        api_keyK = 'fCLPHkET4wnH/xJmfSGW0qnqEeLbH90BJ/WdAigALeaXcwM06LpHNwi90O3C54Gut2wvY28Agl44JLPQFqJLaA=='
        headersK= {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_keyK)}

        reqK= urllib2.Request(urlK, body1, headersK)

      

        


      try:
          response1 = urllib2.urlopen(req1)

          result1 = response1.read()
          resp_dict1 = json.loads(result1)
          print(result1)
          rateOfInterest1=resp_dict1['Results']['output1'][0]['Scored Label Mean']
          
          print("no clustering",rateOfInterest1)


          responseA = urllib2.urlopen(reqA)

          resultA = responseA.read()
          resp_dictA= json.loads(resultA)
          print(resultA)
          rateOfInterestA=resp_dictA['Results']['output1'][0]['Scored Label Mean']
          
          print("grade based",rateOfInterestA)


          responseK = urllib2.urlopen(reqK)

          resultK = responseK.read()
          resp_dictK= json.loads(resultK)
          print(resultK)
          rateOfInterestK=resp_dictK['Results']['output1'][0]['Scored Labels']
          
          print("k means clustering",rateOfInterestK)
      except urllib2.HTTPError, error:
          print("The request failed with status code: " + str(error.code))

          # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
          print(error.info())
          print(json.loads(error.read())) 



    return render_template('regression.html',rateOfInterest1=rateOfInterest1,rateOfInterestA=rateOfInterestA,rateOfInterestK=rateOfInterestK)

  elif request.method == 'GET':
    return render_template('success.html',form=form)













  

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/fetch")
def fetch():
  return render_template("fetch.html")

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
      if(status=='Accepted'):
        return redirect(url_for('success'))
      else:
        return redirect(url_for('fetch'))


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