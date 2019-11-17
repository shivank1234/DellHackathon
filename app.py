from flask import Flask, render_template,request,flash,session,redirect
import pyrebase

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
      return render_template("idea.html")
    else:
      return render_template("signin.html")

@app.route("/Register", methods=["GET", "POST"])
def register():
     if request.method == "POST":
      useremail = request.form["email"]   #Data Extracted from HTML
      password = request.form["password"]
      cpassword = request.form["confirming"]
      if (password != cpassword):
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
    return render_template("product1.html")

@app.route("/product2.html")
def p2():
    return render_template("product2.html")

@app.route("/product3.html")
def p3():
    return render_template("product3.html")

@app.route("/P2info")
def p2():
    return render_template("p2info.html")

@app.route("/P3info")
def p3():
    return render_template("p3info.html")
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
