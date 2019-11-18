import pyrebase
from flask import Flask, render_template,request,flash,session,redirect

app = Flask(__name__)

config = {
    "apiKey": "AIzaSyAdquXgxR_M9NsQpW50vsz0v6WwvvBC17A",
    "authDomain": "dellhackathon-e28e7.firebaseapp.com",
    "databaseURL": "https://dellhackathon-e28e7.firebaseio.com",
    "projectId": "dellhackathon-e28e7",
    "storageBucket": "dellhackathon-e28e7.appspot.com",
    "messagingSenderId": "4547496317",
    "appId": "1:4547496317:web:8f3caa80b97db683e6a414",
    "measurementId": "G-GGYG3JXW08"
  }

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/SignIn",methods=["GET", "POST"])
def signin():
    if request.method == "POST":
      username = request.form["username"]   #Data Extracted from HTML
      password = request.form["pass"]
      try:
      	auth.sign_in_with_email_and_password(email, password)
      except:
	return 'check your credentials
      return render_template("idea.html")
    else:
      return render_template("signin.html")
    

@app.route("/Register")
def register():
    return render_template("register.html")

@app.route("/P1info")
def p1():
    return render_template("p1info.html")

if __name__ == "__main__":
    app.run()

#email = input('please enter email \n')
#password = input('password \n')

#user = auth.create_user_with_email_and_password(email, password)
#auth.send_email_verification(user['idToken'])
#auth.send_password_reset_email(email)
#print(auth.get_account_Info(user['idToken']))

                                   
