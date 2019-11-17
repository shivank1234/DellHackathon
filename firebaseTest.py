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

email = input('please enter email \n')
password = input('password \n')

user = auth.create_user_with_email_and_password(email, password)
#auth.send_email_verification(user['idToken'])
#auth.send_password_reset_email(email)
#print(auth.get_account_Info(user['idToken']))

                                   
