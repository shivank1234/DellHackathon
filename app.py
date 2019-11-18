from flask import Flask, render_template,request,flash,session,redirect
from pyrebase import pyrebase
from textblob import TextBlob
import csv

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
      username = request.form["email"]   #Data Extracted from HTML
      password = request.form["pass"]
      return render_template("idea.html")
    else:
      return render_template("signin.html")

@app.route("/Register", methods=["GET", "POST"])
def register():
     if request.method == "POST":
      useremail = request.form["email"]   #Data Extracted from HTML
      password = request.form["password"]
      cpassword = request.form["confirming"]
      radio1=request.form["radio1"]
      radio2=request.form["radio2"]
      radio3=request.form["radio3"]
      radio4=request.form["radio4"]
      radio5=request.form["radio5"]
      radio6=request.form["radio6"]
      if (password != cpassword) or (len(password)<7):
         return render_template("register1.html")
      else:
         user = auth.create_user_with_email_and_password(useremail, password)  #User created in the Firebase Database
      return render_template("idea.html")
     else:
        return render_template("register1.html")

@app.route("/Idea")
def idea():
    return render_template("idea.html")

@app.route("/product1.html")
def p1():
 with open('dell dataset.csv','r') as csv_file:
           reader=csv.reader(csv_file)
           sudoku_list = list(reader)

 i=1
 max=0
 tmax=-1
 min=0
 tmin=-1
 while (i<99):
    blob = TextBlob(sudoku_list[i][1])
    if(((int(sudoku_list[i][0]))%3)!=0):
      i=i+1
      continue
    for sentence in blob.sentences:
      if(sentence.sentiment.polarity>max):
           tmax=i
    i=i+1

 i=1

 while (i<99):
    blob = TextBlob(sudoku_list[i][1])
    if(((int(sudoku_list[i][0]))%3)!=0):
      i=i+1
      continue
    for sentence in blob.sentences:
      if(sentence.sentiment.polarity<min):
           tmin=i
    i=i+1

 print(sudoku_list[tmax][1])   #Results of Sentiment Analysis
 print(sudoku_list[tmin][1])
 rows = [{"positive":sudoku_list[tmax][1],"negative":sudoku_list[tmin][1]}]



 return render_template("product1.html", rows=rows)

@app.route("/product2.html")
def p2():
    with open('dell dataset.csv','r') as csv_file:
           reader=csv.reader(csv_file)
           sudoku_list = list(reader)

    i=1
    max=0
    tmax=-1
    min=0
    tmin=-1
    while (i<99):
       blob = TextBlob(sudoku_list[i][1])
       if(((int(sudoku_list[i][0]))%3)!=1):
         i=i+1
         continue
       for sentence in blob.sentences:
         if(sentence.sentiment.polarity>max):
           tmax=i
       i=i+1

    i=1

    while (i<99):
       blob = TextBlob(sudoku_list[i][1])
       if(((int(sudoku_list[i][0]))%3)!=1):
         i=i+1
         continue
       for sentence in blob.sentences:
         if(sentence.sentiment.polarity<min):
              tmin=i
       i=i+1

    print(sudoku_list[tmax][1])   #Results of Sentiment Analysis
    print(sudoku_list[tmin][1])
    rows = [{"positive":sudoku_list[tmax][1],"negative":sudoku_list[tmin][1]}]

    return render_template("product2.html",rows=rows)

@app.route("/product3.html")
def p3():
    with open('dell dataset.csv','r') as csv_file:
           reader=csv.reader(csv_file)
           sudoku_list = list(reader)

    i=1
    max=0
    tmax=-1
    min=0
    tmin=-1
    while (i<99):
       blob = TextBlob(sudoku_list[i][1])
       if(((int(sudoku_list[i][0]))%3)!=2):
         i=i+1
         continue
       for sentence in blob.sentences:
         if(sentence.sentiment.polarity>max):
              tmax=i
       i=i+1

    i=1

    while (i<99):
       blob = TextBlob(sudoku_list[i][1])
       if(((int(sudoku_list[i][0]))%3)!=2):
         i=i+1
         continue
       for sentence in blob.sentences:
         if(sentence.sentiment.polarity<min):
              tmin=i
       i=i+1

    print(sudoku_list[tmax][1])   #Results of Sentiment Analysis
    print(sudoku_list[tmin][1])
    rows = [{"positive":sudoku_list[tmax][1],"negative":sudoku_list[tmin][1]}]

    return render_template("product3.html",rows=rows)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
